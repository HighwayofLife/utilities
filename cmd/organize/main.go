package main

import (
	"fmt"
	"image"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/urfave/cli/v2"
)

// const (
// 	landscapeDir    = "landscape"
// 	squareDir       = "square"
// 	portraitDir     = "portrait"
// 	thumbnailWidth  = 300
// 	thumbnailHeight = 300
// )

func main() {
	app := &cli.App{
		Name:  "image_organize",
		Usage: "Organize images by orientation",
		Flags: []cli.Flag{
			&cli.StringFlag{
				Name:     "source",
				Aliases:  []string{"i", "s"},
				Required: true,
				Usage:    "The source (input) directory",
			},
			&cli.StringFlag{
				Name:    "destination",
				Aliases: []string{"o", "d"},
				Usage:   "The destination (output) directory",
			},
			&cli.StringFlag{
				Name:    "landscape-dir",
				Aliases: []string{"l"},
				Value:   "landscape",
				Usage:   "The landscape directory name",
			},
			&cli.StringFlag{
				Name:    "square-dir",
				Aliases: []string{"sq"},
				Value:   "square",
				Usage:   "The square directory name",
			},
			&cli.StringFlag{
				Name:    "portrait-dir",
				Aliases: []string{"p"},
				Value:   "portrait",
				Usage:   "The portrait directory name",
			},
			&cli.BoolFlag{
				Name:    "verbose",
				Aliases: []string{"v"},
				Usage:   "Verbose mode",
			},
		},
		Action: func(c *cli.Context) error {
			start := time.Now()

			sourceDir := c.String("source")
			destinationDir := c.String("destination")
			landscapeDir := c.String("landscape-dir")
			squareDir := c.String("square-dir")
			portraitDir := c.String("portrait-dir")
			verbose := c.Bool("verbose")

			if destinationDir == "" {
				destinationDir = sourceDir
			}

			if _, err := os.Stat(sourceDir); os.IsNotExist(err) {
				return fmt.Errorf("source directory '%s' does not exist", sourceDir)
			}

			createDirectories(destinationDir, landscapeDir, squareDir, portraitDir)

			filesMoved, err := organizeImages(sourceDir, destinationDir, landscapeDir, squareDir, portraitDir, verbose)
			if err != nil {
				return err
			}

			fmt.Printf("Done! Organization complete. %d files moved to %s\n", filesMoved, destinationDir)

			elapsed := time.Since(start)
			fmt.Printf("Time elapsed: %s\n", elapsed)

			return nil
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}

func createDirectories(destinationDir string, dirs ...string) {
	os.Mkdir(destinationDir, os.ModePerm)

	for _, dir := range dirs {
		os.MkdirAll(filepath.Join(destinationDir, dir), os.ModePerm)
	}
}

func organizeImages(sourceDir, destinationDir, landscapeDir, squareDir, portraitDir string, verbose bool) (int, error) {

	// Validate that the sourceDir exists
	if _, err := os.Stat(sourceDir); os.IsNotExist(err) {
		return 0, fmt.Errorf("source directory '%s' does not exist", sourceDir)
	}

	filesMoved := 0

	err := filepath.Walk(sourceDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() {
			return nil
		}

		if !strings.HasSuffix(strings.ToLower(info.Name()), ".jpg") && !strings.HasSuffix(strings.ToLower(info.Name()), ".jpeg") && !strings.HasSuffix(strings.ToLower(info.Name()), ".png") {
			return nil
		}

		file, err := os.Open(path)
		if err != nil {
			return err
		}
		defer file.Close()

		img, _, err := image.Decode(file)
		if err != nil {
			return err
		}

		width := img.Bounds().Dx()
		height := img.Bounds().Dy()

		var destinationDir string

		if width > height {
			destinationDir = landscapeDir
		} else if width < height {
			destinationDir = portraitDir
		} else {
			destinationDir = squareDir
		}

		if verbose {
			fmt.Printf("Moving %s to %s\n", info.Name(), filepath.Join(destinationDir, info.Name()))
		}

		err = moveFile(path, filepath.Join(destinationDir, info.Name()))
		if err != nil {
			return err
		}

		filesMoved++

		return nil
	})

	if err != nil {
		return 0, err
	}

	return filesMoved, nil
}

func walkFunc(path string, info os.FileInfo, err error) error {
	if err != nil {
			return err
	}

	if info.IsDir() {
			return nil
	}

	if !strings.HasSuffix(strings.ToLower(info.Name()), ".jpg") && !strings.HasSuffix(strings.ToLower(info.Name()), ".jpeg") && !strings.HasSuffix(strings.ToLower(info.Name()), ".png") {
			return nil
	}

	filesMoved := 0

	file, err := os.Open(path)
	if err != nil {
			return err
	}
	defer file.Close()

	img, _, err := image.Decode(file)
	if err != nil {
			return err
	}

	width := img.Bounds().Dx()
	height := img.Bounds().Dy()

	var destinationDir string

	if width > height {
			destinationDir = landscapeDir
	} else if width < height {
			destinationDir = portraitDir
	} else {
			destinationDir = squareDir
	}

	if verbose {
			fmt.Printf("Moving %s to %s\n", info.Name(), filepath.Join(destinationDir, info.Name()))
	}

	err = moveFile(path, filepath.Join(destinationDir, info.Name()))
	if err != nil {
			return err
	}

	filesMoved++
	fmt.Printf("Moved %d files\n", filesMoved)

	return nil
}

func moveFile(source, destination string) error {
	input, err := os.ReadFile(source)
	if err != nil {
		return err
	}

	err = os.WriteFile(destination, input, 0644)
	if err != nil {
		return err
	}

	return os.Remove(source)
}
