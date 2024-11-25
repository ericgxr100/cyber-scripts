# Metadata Extractor

## Description
A Python script to extract metadata from image files (JPEG, PNG) using the `Pillow` library.

## Features
- Recursively scans directories for image files.
- Extracts and displays metadata from images.

## How to Use
1. Run the script:
   ```bash
   python metadata_extractor.py
   ```
2. Enter the directory path containing the images.
3. The script will display metadata for each file.

## Requirements
- Python 3.x
- `Pillow` library (install with `pip install pillow`)

## Example Output
```plaintext
Extracting metadata from: photo.jpg
Make: Canon
Model: EOS 80D
DateTime: 2022:01:15 12:34:56
```
