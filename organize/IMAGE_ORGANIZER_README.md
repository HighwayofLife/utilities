# Image Organizer

This script organizes images by their orientation (landscape, square, or portrait). It takes a source directory and an optional destination directory as input, and creates three subdirectories within the destination directory to store the organized images.

## Usage

To use this script, you'll need to have Python 3 and the Pillow library installed. You can install Pillow using pip:

```
pip install Pillow
```

Once you have the prerequisites installed, you can run the script using the following command:

```
python image_organize.py --source /path/to/source/directory --destination /path/to/destination/directory
```

You can also specify custom directory names for the landscape, square, and portrait subdirectories using the `--landscape-dir`, `--square-dir`, and `--portrait-dir` options, respectively.

### Parameters

| Name | Description | Required |
| --- | --- | --- |
| `--source`, `-i`, `--input`, `--src`, `--s` | The source (input) directory. | Yes |
| `--destination`, `-o`, `--output`, `--dest`, `--d` | The destination (output) directory. If not specified, defaults to the source directory. | No |
| `--landscape-dir`, `-l`, `--landscape` | The name of the directory to store landscape images. If not specified, defaults to "landscape". | No |
| `--square-dir`, `-sq`, `--square` | The name of the directory to store square images. If not specified, defaults to "square". | No |
| `--portrait-dir`, `-p`, `--portrait` | The name of the directory to store portrait images. If not specified, defaults to "portrait". | No |

## License

This script is released under the MIT License. See LICENSE.txt for details.
