import os
import argparse
import time
from PIL import Image


class Args:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def convert_webp(source_folder, destination_folder):
    start_time = time.time()
    for filename in os.listdir(source_folder):
        if filename.endswith(".webp"):
            with Image.open(os.path.join(source_folder, filename)) as im:
                png_image = os.path.splitext(filename)[0] + ".png"
                im.save(os.path.join(destination_folder, png_image), "PNG")
    end_time = time.time()
    print(f"Converted images in {end_time - start_time:.2f} seconds")


def main():
    parser = argparse.ArgumentParser(description="Convert .webp images to .png")
    # Default argument, as well as -i, or --input are all the source/input folder
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to the source folder",
    )
      
    
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        help="(Optional) Path to the destination folder, will use the source folder by default.",
    )
    args = parser.parse_args()

    source_folder = args.input

    if args.output is None:
        destination_folder = source_folder
    else:
        destination_folder = args.output

    convert_webp(source_folder, destination_folder)


# # Directory containing .webp images
# img_dir = "/path/to/your/images"

# # Get a list of all .webp files in the directory
# webp_images = [f for f in os.listdir(img_dir) if f.endswith('.webp')]

# # Convert each .webp image to .png
# for webp_image in webp_images:
#     img = Image.open(os.path.join(img_dir, webp_image))
#     png_image = os.path.splitext(webp_image)[0] + ".png"  # change extension to .png
#     img.save(os.path.join(img_dir, png_image), "PNG")  # save the image in PNG format

# print("Conversion completed!")
