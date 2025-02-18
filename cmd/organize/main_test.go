package main

import (
	"image"
	"image/color"
	"image/jpeg"
	"os"
	"path/filepath"
	"testing"
)

func TestOrganizeImages(t *testing.T) {
	// Setup the test environment
	tempDir, cleanup := setup(t)
	defer cleanup()

	// Call the function being tested
	destinationDir := filepath.Join(tempDir, "output")
	landscapeDir := "landscape"
	squareDir := "square"
	portraitDir := "portrait"
	_, err := organizeImages(tempDir, destinationDir, landscapeDir, squareDir, portraitDir, false)
	if err != nil {
		t.Fatal(err)
	}

	// Check that the files were moved to the correct directories
	checkFiles := []struct {
		name     string
		expected string
	}{
		{"landscape.jpg", landscapeDir},
		{"portrait.jpg", portraitDir},
		{"square.jpg", squareDir},
		{"not_an_image.txt", ""},
	}
	for _, cf := range checkFiles {
		filePath := filepath.Join(destinationDir, cf.expected, cf.name)
		if cf.expected == "" {
			// Non-image files should not be moved
			if _, err := os.Stat(filePath); !os.IsNotExist(err) {
				t.Errorf("Expected file '%s' to not exist, but it does", filePath)
			}
		} else {
			// Image files should be moved to the correct directory
			if _, err := os.Stat(filePath); os.IsNotExist(err) {
				t.Errorf("Expected file '%s' to exist, but it does not", filePath)
			}
		}
	}
}

func setup(t *testing.T) (string, func()) {
	// Create a temporary directory for testing
	tempDir, err := os.MkdirTemp("", "test")
	if err != nil {
		t.Fatal(err)
	}

	// Create some test files in the temporary directory
	testFiles := []struct {
		name   string
		width  int
		height int
	}{
		{"landscape.jpg", 800, 600},
		{"portrait.jpg", 600, 800},
		{"square.jpg", 500, 500},
		{"not_an_image.txt", 0, 0},
	}
	for _, tf := range testFiles {
		filePath := filepath.Join(tempDir, tf.name)
		if tf.width > 0 && tf.height > 0 {
			// Create a test image file
			img := createTestImage(tf.width, tf.height)
			err := saveTestImage(img, filePath)
			if err != nil {
				t.Fatal(err)
			}
		} else {
			// Create a test non-image file
			err := os.WriteFile(filePath, []byte("not an image"), 0644)
			if err != nil {
				t.Fatal(err)
			}
		}
	}

	// Return the temporary directory path and a cleanup function
	return tempDir, func() {
		os.RemoveAll(tempDir)
	}
}

func createTestImage(width, height int) image.Image {
	img := image.NewRGBA(image.Rect(0, 0, width, height))
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			img.Set(x, y, color.RGBA{uint8(x), uint8(y), 0, 255})
		}
	}
	return img
}

func saveTestImage(img image.Image, filePath string) error {
	file, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	err = jpeg.Encode(file, img, &jpeg.Options{Quality: 100})
	if err != nil {
		return err
	}

	return nil
}
