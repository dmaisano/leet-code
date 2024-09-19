package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/dmaisano/leet-code/utils"
)

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

func isDigit(char string) bool {
	_, err := strconv.Atoi(char)
	return err == nil
}

func part1Soln(lines []string) int {
	totalSum := 0
	for _, line := range lines {
		firstDigit := ""
		lastDigit := ""

		for _, char := range line {
			if isDigit(string(char)) {
				firstDigit = string(char)
				break
			}
		}

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

func part2Soln(calibrationDocument []string) int {
	totalSum := 0
	for _, line := range calibrationDocument {
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
		totalSum += num

	}
	return totalSum
}

func main() {
	lines, _ := utils.ReadFileLines("/home/virtualdom/projects/leet-code/advent_of_code/2023/day_1/day_1.txt")

	part1 := part1Soln(lines)
	part2 := part2Soln(lines)

	fmt.Printf("Part 1: %d\n", part1) // 54338
	fmt.Printf("Part 2: %d\n", part2) // 53389
}
