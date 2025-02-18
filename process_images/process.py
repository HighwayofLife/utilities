import argparse
from PIL import Image
import os
import time

def resize_image(source_folder, destination_folder):
    start_time = time.time()
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            with Image.open(os.path.join(source_folder, filename)) as im:
                width, height = im.size
                new_size = (int(width/2), int(height/2))
                resized_im = im.resize(new_size)
                resized_im.save(os.path.join(destination_folder, filename))
    end_time = time.time()
    print(f"Resized images in {end_time - start_time:.2f} seconds")

def main():
    parser = argparse.ArgumentParser(description='Resize images in a folder and save them to a destination folder')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the source folder')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the destination folder')
    args = parser.parse_args()

    source_folder = args.input
    destination_folder = args.output
    resize_image(source_folder, destination_folder)

if __name__ == "__main__":
    main()