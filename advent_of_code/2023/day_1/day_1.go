package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/dmaisano/leet-code/utils"
)

// A map to convert word digits to numeric digits.
var digitMapping = map[string]string{
	"one":   "1",
	"two":   "2",
	"three": "3",
	"four":  "4",
	"five":  "5",
	"six":   "6",
	"seven": "7",
	"eight": "8",
	"nine":  "9",
}

// sumCalibrationValuesPart1 sums the values by finding the first and last digits in each line.
func sumCalibrationValuesPart1(lines []string) int {
	totalSum := 0
	for _, line := range lines {
		firstDigit := ""
		lastDigit := ""
		// Find the first digit
		for _, char := range line {
			if isDigit(string(char)) {
				firstDigit = string(char)
				break
			}
		}

		// Find the last digit
		for i := len(line) - 1; i >= 0; i-- {
			if isDigit(string(line[i])) {
				lastDigit = string(line[i])
				break
			}
		}

		if firstDigit != "" && lastDigit != "" {
			num, _ := strconv.Atoi(firstDigit + lastDigit)
			totalSum += num
		}
	}
	return totalSum
}

// sumCalibrationValuesPart2 sums the values using the digit mapping and parsing logic.
func sumCalibrationValuesPart2(calibrationDocument []string) int {
	totalSum := 0
	for _, line := range calibrationDocument {
		totalSum += parseLine(line)
	}
	return totalSum
}

// parseLine parses the line to find the first and last digits, including words representing digits.
func parseLine(line string) int {
	var digits []string

	for i := 0; i < len(line); i++ {
		char := string(line[i])

		if isDigit(char) {
			digits = append(digits, char)
			continue
		}

		subStr := line[i:]
		for key, value := range digitMapping {
			if strings.HasPrefix(subStr, key) {
				digits = append(digits, value)
				break
			}
		}
	}

	num, _ := strconv.Atoi(digits[0] + digits[len(digits)-1])
	return num
}

// isDigit checks if a character is a digit.
func isDigit(char string) bool {
	_, err := strconv.Atoi(char)
	return err == nil
}

func main() {
	lines, _ := utils.ReadFileLines("/home/virtualdom/projects/leet-code/advent_of_code/2023/day_1/day_1.txt")

	part1Points := sumCalibrationValuesPart1(lines)
	part2Points := sumCalibrationValuesPart2(lines)

	fmt.Printf("Part 1 total points: %d\n", part1Points)
	fmt.Printf("Part 2 total points: %d\n", part2Points)
}
