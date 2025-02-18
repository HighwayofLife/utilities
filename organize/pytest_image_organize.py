import os
import shutil
from PIL import Image
import pytest
from image_organize import organize_images

class Args:
  def __init__(self, source, destination, landscape_dir, square_dir, portrait_dir, verbose):
    self.source = source
    self.destination = destination
    self.landscape_dir = landscape_dir
    self.square_dir = square_dir
    self.portrait_dir = portrait_dir
    self.verbose = verbose
    


@pytest.fixture(scope="module")
def test_data(tmpdir_factory):
    # Create a temporary directory for the test data
    test_dir = tmpdir_factory.mktemp("test_data")

    # Create some test images
    landscape_img = Image.new("RGB", (800, 600), color="red")
    landscape_img.save(os.path.join(test_dir, "landscape.jpg"))

    square_img = Image.new("RGB", (600, 600), color="green")
    square_img.save(os.path.join(test_dir, "square.jpg"))

    portrait_img = Image.new("RGB", (400, 600), color="blue")
    portrait_img.save(os.path.join(test_dir, "portrait.jpg"))

    # Return the path to the test directory
    return str(test_dir)


def test_organize_images(test_data):
    # Set up the arguments for the organize_images function

    args = Args(source=test_data, destination=None, landscape_dir=None, square_dir=None, portrait_dir=None, verbose=False)
    args.source = test_data
    args.verbose = False

    # Call the organize_images function
    organize_images(args)

    # Check that the images were moved to the correct directories
    assert os.path.exists(os.path.join(test_data, "landscape", "landscape.jpg"))
    assert os.path.exists(os.path.join(test_data, "square", "square.jpg"))
    assert os.path.exists(os.path.join(test_data, "portrait", "portrait.jpg"))

    # Clean up the test data
    shutil.rmtree(test_data)
