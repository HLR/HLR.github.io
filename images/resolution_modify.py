from PIL import Image
import os


def compress_image(input_path, output_path, target_size_mb=2, step=5, min_quality=20):
    img = Image.open(input_path)
    quality = 95  # start high
    target_size = target_size_mb * 1024 * 1024

    while quality >= min_quality:
        # Save the image with current quality setting
        img.save(output_path, "JPEG", quality=quality, optimize=True)
        current_size = os.path.getsize(output_path)

        if current_size <= target_size:
            print(
                f"Compressed successfully to {current_size / 1024 / 1024:.2f} MB at quality={quality}"
            )
            return

        quality -= step

    print(
        "Couldn't reach target size with acceptable quality. Consider resizing the image."
    )


# Example usage
compress_image(
    "/Users/sue/HLR/ResumeWebsite/HLR.github.io/images/picpic/Gallery/NLP_DAY_speak.jpg",
    "/Users/sue/HLR/ResumeWebsite/HLR.github.io/images/picpic/Gallery/NLP_DAY_speak_compressed.jpg",
)
