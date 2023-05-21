import os
import shutil
import unittest
from PIL import Image
from image_organize import organize_images


class Args:
    def __init__(
        self, source, destination, landscape_dir, square_dir, portrait_dir, verbose
    ):
        self.source = source
        self.destination = destination
        self.landscape_dir = landscape_dir
        self.square_dir = square_dir
        self.portrait_dir = portrait_dir
        self.verbose = verbose


class TestImageOrganize(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_images"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create some test images
        img1 = Image.new("RGB", (100, 50), color="red")
        img1.save(os.path.join(self.test_dir, "img1.jpg"))
        img2 = Image.new("RGB", (50, 100), color="green")
        img2.save(os.path.join(self.test_dir, "img2.jpg"))
        img3 = Image.new("RGB", (50, 50), color="blue")
        img3.save(os.path.join(self.test_dir, "img3.jpg"))

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_organize_images(self):
        # Call the organize_images function with the test directory as the source
        args = Args(
            source=self.test_dir,
            destination="test_output",
            landscape_dir="test_landscape",
            square_dir="test_square",
            portrait_dir="test_portrait",
            verbose=False,
        )
        organize_images(args)

        # Check that the output directory was created
        self.assertTrue(os.path.exists("test_output"))

        # Check the other directories to ensure they exist
        self.assertTrue(os.path.exists(os.path.join("test_output", "test_landscape")))
        self.assertTrue(os.path.exists(os.path.join("test_output", "test_portrait")))
        self.assertTrue(os.path.exists(os.path.join("test_output", "test_square")))

        # Check that the images were moved to the correct directories
        self.assertTrue(
            os.path.exists(os.path.join("test_output", "test_landscape", "img1.jpg"))
        )
        self.assertTrue(
            os.path.exists(os.path.join("test_output", "test_portrait", "img2.jpg"))
        )
        self.assertTrue(
            os.path.exists(os.path.join("test_output", "test_square", "img3.jpg"))
        )


if __name__ == "__main__":
    unittest.main()
