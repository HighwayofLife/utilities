# Image Organizer

This script organizes images by their orientation (landscape, square, or portrait) and moves them to their respective directories.

## Usage

```bash
python image_organize.py --source /path/to/source/directory \
	--destination /path/to/destination/directory
```

## Arguments

| Name | Description | Required |
| --- | --- | --- |
| --source, --input, --i, --src, --s | The source (input) directory. | Yes |
| --destination, --output, --o, --dest, --d | The destination (output) directory. If not specified, the script will use the source directory. | No |
| --landscape-dir, --landscape, --l | The landscape directory name. If not specified, the script will use "landscape". | No |
| --square-dir, --square, --sq | The square directory name. If not specified, the script will use "square". | No |
| --portrait-dir, --portrait, --p | The portrait directory name. If not specified, the script will use "portrait". | No |
| --verbose, --ver, --v | Verbose mode. If specified, the script will print the name of each file as it is moved. | No |


The script takes in a source directory containing images and organizes them into three directories based on their orientation: landscape, square, and portrait. The user can specify the source directory and the names of the three destination directories. If the destination directory is not specified, the script will use the source directory. If the names of the destination directories are not specified, the script will use "landscape", "square", and "portrait" as the default names.


- The `--source` argument is required and specifies the source directory containing the images to be organized.
- The `--destination` argument is optional and specifies the destination directory where the organized images will be moved to. If not specified, the script will use the source directory as the destination directory.
- The `--landscape-dir`, `--square-dir`, and `--portrait-dir` arguments are optional and specify the names of the three destination directories.
- If not specified, the script will use "landscape", "square", and "portrait" as the default names.
- The `--verbose` argument is optional and specifies whether the script should print the name of each file as it is moved.

## Testing

To run the tests on the script, simply run:
```bash
python test_image_organize.py
```

## LICENSE

This script is licensed under the MIT License.
