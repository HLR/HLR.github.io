#!/usr/bin/env python3
"""Regression checks for the NeSy 2026 AgenticDomiKnowS publication."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
TITLE = "An Agentic Framework for Neuro-Symbolic Programming"
ARXIV_URL = "https://arxiv.org/abs/2601.00743"
PDF_URL = "https://arxiv.org/pdf/2601.00743"


class PublicationParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.text_parts: list[str] = []
        self.links: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)


class NeSy2026PublicationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.site_directory = Path(cls.temporary_directory.name) / "site"
        subprocess.run(
            [
                "bundle",
                "exec",
                "jekyll",
                "build",
                "--destination",
                str(cls.site_directory),
            ],
            cwd=REPO_ROOT,
            check=True,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary_directory.cleanup()

    def test_publication_page_lists_nesy_2026_paper(self) -> None:
        parser = PublicationParser()
        parser.feed((self.site_directory / "publications" / "index.html").read_text())
        visible_text = " ".join(" ".join(parser.text_parts).split())

        self.assertIn(TITLE, visible_text)
        self.assertIn(
            "Aliakbar Nafar, Chetan Chigurupati, Danial Kamali, "
            "Hamid Karimian, Parisa Kordjamshidi",
            visible_text,
        )
        self.assertIn(
            "20th International Conference on Neurosymbolic Learning and "
            "Reasoning (NeSy 2026)",
            visible_text,
        )
        self.assertIn(PDF_URL, parser.links)

    def test_downloadable_bibtex_includes_nesy_2026_paper(self) -> None:
        bibtex = (self.site_directory / "downloads" / "hlr.bib").read_text()

        self.assertIn("@inproceedings{nafar2026agentic", bibtex)
        self.assertIn(
            "title={An Agentic Framework for Neuro-Symbolic Programming}",
            bibtex,
        )
        self.assertIn(
            "booktitle={Proceedings of the 20th International Conference on",
            bibtex,
        )
        self.assertIn("eprint={2601.00743}", bibtex)
        self.assertIn(f"url={{{ARXIV_URL}}}", bibtex)


if __name__ == "__main__":
    unittest.main()
