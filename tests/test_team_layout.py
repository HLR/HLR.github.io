#!/usr/bin/env python3
"""Browser regression check for the PhD-student card text column."""

from __future__ import annotations

import http.server
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading


REPO_ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def chrome_binary() -> str:
    candidates = (
        os.environ.get("CHROME_BIN"),
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    )
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise RuntimeError("Chrome or Chromium is required for this layout test")


def main() -> None:
    with tempfile.TemporaryDirectory() as temporary_directory:
        site_directory = Path(temporary_directory) / "site"
        subprocess.run(
            ["bundle", "exec", "jekyll", "build", "--destination", str(site_directory)],
            cwd=REPO_ROOT,
            check=True,
        )

        team_page = site_directory / "team" / "index.html"
        probe = """
<script>
(() => {
  const failures = [...document.querySelectorAll('.phd-student-card')]
    .flatMap((card) => {
      const image = card.querySelector('img');
      const details = card.querySelector('.phd-student-details');
      const detailsParagraph = details.querySelector('p');
      const range = document.createRange();
      range.selectNodeContents(details);
      const textRects = [...range.getClientRects()]
        .filter((rect) => rect.width > 0 && rect.height > 0);
      const imageRect = image.getBoundingClientRect();
      const detailsRect = details.getBoundingClientRect();
      const dimensionsAreValid = imageRect.width > 0 && detailsRect.width > 0;
      const textStaysBesideImage = textRects.length > 0
        && textRects.every((rect) => rect.left >= imageRect.right);
      const detailsAreLeftAligned = getComputedStyle(detailsParagraph).textAlign === 'left';
      if (dimensionsAreValid && textStaysBesideImage && detailsAreLeftAligned) {
        return [];
      }
      return [{
        name: card.querySelector('h4').textContent.trim(),
        imageRight: imageRect.right,
        minimumTextLeft: Math.min(...textRects.map((rect) => rect.left)),
        textAlign: getComputedStyle(detailsParagraph).textAlign,
        textRectCount: textRects.length,
      }];
    });
  const result = document.createElement('div');
  result.id = 'team-layout-test-result';
  result.textContent = failures.length === 0 ? 'PASS' : 'FAIL';
  result.dataset.viewportWidth = innerWidth;
  result.dataset.failures = JSON.stringify(failures);
  document.body.appendChild(result);
})();
</script>
"""
        team_page.write_text(
            team_page.read_text().replace("</body>", f"{probe}</body>"),
        )

        handler = lambda *args, **kwargs: QuietHandler(
            *args, directory=str(site_directory), **kwargs
        )
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for viewport_width in (1016, 375):
                result = subprocess.run(
                    [
                        chrome_binary(),
                        "--headless=new",
                        "--disable-gpu",
                        "--no-sandbox",
                        f"--window-size={viewport_width},900",
                        "--virtual-time-budget=5000",
                        "--dump-dom",
                        f"http://127.0.0.1:{server.server_port}/team/",
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )

                marker = 'id="team-layout-test-result"'
                if marker not in result.stdout or ">PASS</div>" not in result.stdout:
                    diagnostic = next(
                        (line.strip() for line in result.stdout.splitlines() if marker in line),
                        "layout result marker missing",
                    )
                    raise AssertionError(
                        f"PhD details escape their text columns at "
                        f"{viewport_width}px: {diagnostic}"
                    )
        finally:
            server.shutdown()

        print("PASS: PhD details remain left-aligned beside portraits at 1016px and 375px")


if __name__ == "__main__":
    main()
