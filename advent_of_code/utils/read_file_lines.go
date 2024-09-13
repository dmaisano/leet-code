package utils

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// ReadFileLines reads a text file and returns a slice of its non-empty lines.
func ReadFileLines(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("error opening file: %v", err)
	}
	defer file.Close()

	// Read the file line by line and filter non-empty lines.
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}

	// Check for any scanning errors.
	if err := scanner.Err(); err != nil {
		fmt.Println("error scanning file:", err)
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	return lines, nil
}
