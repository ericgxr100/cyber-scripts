from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_metadata(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                print(f"{tag_name}: {value}")
        else:
            print("No metadata found.")
    except Exception as e:
        print(f"Error reading metadata: {e}")

def main():
    directory = input("Enter the directory containing images: ")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(f"\nExtracting metadata from: {file}")
                extract_metadata(os.path.join(root, file))

if __name__ == "__main__":
    main()
