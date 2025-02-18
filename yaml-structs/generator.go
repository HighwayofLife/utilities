package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"

	"gopkg.in/yaml.v3"
	"github.com/twpayne/go-jsonstruct/v2"
)

func main() {
	var typeName, inputFile, outputFile string

	flag.StringVar(&typeName, "type", "", "type name; Name of the root struct")
	flag.StringVar(&inputFile, "in", "", "input file; Path to the YAML file")
	flag.StringVar(&outputFile, "out", "", "output file; Path to output Go file")

	flag.Parse()

	if typeName == "" || inputFile == "" || outputFile == "" {
		flag.Usage()
		os.Exit(1)
	}

	yamlData, err := os.ReadFile(inputFile)
	if err != nil {
		fmt.Printf("ERror reading YAML file: %s", err)
		os.Exit(1)
	}

	var jsonData map[string]interface{}
	err = yaml.Unmarshal(yamlData, &jsonData)
	if err != nil {
		fmt.Printf("Error unmarshalling YAML data: %s", err)
		os.Exit(1)
	}

	jsonDataBytes, err := json.Marshal(jsonData)
	if err != nil {
		fmt.Printf("Error marshalling JSON data: %s", err)
		os.Exit(1)
	}

	generatedCode, err := gojsonstruct 
}
