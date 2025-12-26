#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pdf2image>=1.16.3",
#     "pillow>=10.1.0",
# ]
# ///
"""
Generate thumbnails from publication PDFs.
Run before Quarto render to create thumbnail.jpg for each publication.
"""
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image
import sys

PUBLICATIONS_DIR = Path(__file__).parent.parent / "publications"
THUMBNAIL_SIZE = (200, 260)  # Width x Height
DPI = 150
QUALITY = 85

def generate_thumbnail(pdf_path, output_path):
    """Generate thumbnail from first page of PDF."""
    if output_path.exists():
        print(f"  Skipping {pdf_path.name} (thumbnail exists)")
        return True

    try:
        # Convert first page only
        images = convert_from_path(str(pdf_path), dpi=DPI, first_page=1, last_page=1)
        if images:
            img = images[0]
            # Resize maintaining aspect ratio
            img.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            # Save as JPEG
            img.save(str(output_path), "JPEG", quality=QUALITY, optimize=True)
            print(f"  ✓ Generated thumbnail for {pdf_path.name}")
            return True
    except Exception as e:
        print(f"  ✗ Error generating thumbnail for {pdf_path.name}: {e}")
        return False

def main():
    if not PUBLICATIONS_DIR.exists():
        print(f"Error: Publications directory not found: {PUBLICATIONS_DIR}")
        sys.exit(1)

    print("Generating publication thumbnails...")
    print(f"Publications directory: {PUBLICATIONS_DIR}")

    generated = 0
    skipped = 0
    errors = 0
    no_pdf = 0

    for pub_dir in sorted(PUBLICATIONS_DIR.iterdir()):
        if not pub_dir.is_dir() or pub_dir.name.startswith('.'):
            continue

        # Find PDF file
        pdf_files = list(pub_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"  - No PDF found in {pub_dir.name}")
            no_pdf += 1
            continue

        pdf_path = pdf_files[0]
        thumbnail_path = pub_dir / "thumbnail.jpg"

        if thumbnail_path.exists():
            skipped += 1
        else:
            generated += 1

        if not generate_thumbnail(pdf_path, thumbnail_path):
            errors += 1

    print(f"\nSummary:")
    print(f"  Generated: {generated}")
    print(f"  Skipped (existing): {skipped}")
    print(f"  Errors: {errors}")
    print(f"  No PDF: {no_pdf}")

    if errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
