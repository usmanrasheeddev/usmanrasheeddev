from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import remove


def prep_photo(input_path):
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Image not found: {input_path}")

    output_path = input_path.with_name(
        input_path.stem + "-prepped.png"
    )

    print("Removing background...")

    # Load image
    img = Image.open(input_path)

    # Remove background
    subject = remove(img)

    # Create white background
    background = Image.new("RGBA", subject.size, "white")
    combined = Image.alpha_composite(background, subject)

    # Convert to RGB
    combined = combined.convert("RGB")

    # Convert numpy
    img_array = np.array(combined)

    # Grayscale
    gray = cv2.cvtColor(
        img_array,
        cv2.COLOR_RGB2GRAY
    )

    # Improve contrast using CLAHE
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Save
    cv2.imwrite(
        str(output_path),
        enhanced
    )

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python prep_photo.py image.jpg"
        )
        sys.exit(1)

    prep_photo(sys.argv[1])
