import os
from PIL import Image
import argparse
import time


# Set application version
__version__ = "1.0.0"

SOURCE_DIR = ""
DESTINATION_DIR = ""
DESTINATION_LANDSCAPE_DIR = "landscape"
DESTINATION_SQUARE_DIR = "square"
DESTINATION_PORTRAIT_DIR = "portrait"


def set_configs(args):
    global SOURCE_DIR
    global DESTINATION_DIR
    global DESTINATION_LANDSCAPE_DIR
    global DESTINATION_SQUARE_DIR
    global DESTINATION_PORTRAIT_DIR

    SOURCE_DIR = args.source

    if args.destination:
        DESTINATION_DIR = args.destination
    elif os.environ.get("DESTINATION_DIR"):
        DESTINATION_DIR = os.environ.get("DESTINATION_DIR")
    else:
        DESTINATION_DIR = SOURCE_DIR

    if args.landscape_dir:
        DESTINATION_LANDSCAPE_DIR = args.landscape_dir
    elif os.environ.get("LANDSCAPE_DIR"):
        DESTINATION_LANDSCAPE_DIR = os.environ.get("LANDSCAPE_DIR")

    if args.square_dir:
        DESTINATION_SQUARE_DIR = args.square_dir
    elif os.environ.get("SQUARE_DIR"):
        DESTINATION_SQUARE_DIR = os.environ.get("SQUARE_DIR")

    if args.portrait_dir:
        DESTINATION_PORTRAIT_DIR = args.portrait_dir
    elif os.environ.get("PORTRAIT_DIR"):
        DESTINATION_PORTRAIT_DIR = os.environ.get("PORTRAIT_DIR")


def create_directories():
    global DESTINATION_DIR
    global DESTINATION_LANDSCAPE_DIR
    global DESTINATION_SQUARE_DIR
    global DESTINATION_PORTRAIT_DIR

    # Create the directories if they don't exist
    os.makedirs(DESTINATION_DIR, exist_ok=True)
    os.makedirs(os.path.join(DESTINATION_DIR, DESTINATION_LANDSCAPE_DIR), exist_ok=True)
    os.makedirs(os.path.join(DESTINATION_DIR, DESTINATION_SQUARE_DIR), exist_ok=True)
    os.makedirs(os.path.join(DESTINATION_DIR, DESTINATION_PORTRAIT_DIR), exist_ok=True)


def organize_images(args):
    set_configs(args)

    if not os.path.exists(SOURCE_DIR):
        raise ValueError(f"Source directory '{SOURCE_DIR}' does not exist.")

    create_directories()

    print("Organizing images...")
    print("Source directory: {}".format(SOURCE_DIR))
    print("Destination directory: {}".format(DESTINATION_DIR))
    print("Landscape directory: {}".format(DESTINATION_LANDSCAPE_DIR))
    print("Square directory: {}".format(DESTINATION_SQUARE_DIR))
    print("Portrait directory: {}".format(DESTINATION_PORTRAIT_DIR))

    for filename in os.listdir(SOURCE_DIR):
        # We're only interested in images, not other kind of files.
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ):
            with Image.open(os.path.join(SOURCE_DIR, filename)) as img:
                width, height = img.size

            if width > height:  # Landscape
                destination_dir = DESTINATION_LANDSCAPE_DIR
            elif width == height:  # Square
                destination_dir = DESTINATION_SQUARE_DIR
            else:  # Portrait
                destination_dir = DESTINATION_PORTRAIT_DIR

            # Move the file
            if args.verbose:
                print(
                    f"Moving {filename} to {os.path.join(DESTINATION_DIR, destination_dir)}"
                )

            os.rename(
                os.path.join(SOURCE_DIR, filename),
                os.path.join(DESTINATION_DIR, destination_dir, filename),
            )

    print("Done! Organization complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize images by orientation.")
    parser.add_argument(
        "--source",
        "--input",
        "--i",
        "--src",
        "--s",
        required=True,
        type=str,
        help="The source (input) directory.",
    )
    parser.add_argument(
        "--destination",
        "--output",
        "--o",
        "--dest",
        "--d",
        required=False,
        type=str,
        help="The destination (output) directory.",
    )
    parser.add_argument(
        "--landscape-dir",
        "--landscape",
        "--l",
        required=False,
        type=str,
        help="The landscape directory name.",
    )
    parser.add_argument(
        "--square-dir",
        "--square",
        "--sq",
        required=False,
        type=str,
        help="The square directory name.",
    )
    parser.add_argument(
        "--portrait-dir",
        "--portrait",
        "--p",
        required=False,
        type=str,
        help="The portrait directory name.",
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )
    parser.add_argument(
        "--verbose", "--ver", "--v", action="store_true", help="Verbose mode."
    )
    args = parser.parse_args()

    # Time the script
    # Set the start time...
    start_time = time.time()

    organize_images(args)

    end_time = time.time()

    print("Time elapsed: {:.2f}s".format(end_time - start_time))
