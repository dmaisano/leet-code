package main

import (
	"fmt"
	"strconv"
	"unicode"

	"github.com/dmaisano/leet-code/utils"
)

type Token struct {
	value     int
	positions [][2]int
}

func parseGrid(lines []string) ([]Token, map[[2]int]bool, int, int) {
	numbers := []Token{}
	symbols := make(map[[2]int]bool)
	height := len(lines)
	width := 0
	if height > 0 {
		width = len(lines[0])
	}

	for y, line := range lines {
		x := 0
		for x < len(line) {
			ch := rune(line[x])
			if unicode.IsDigit(ch) {
				numStr := ""
				positions := [][2]int{}
				for x < len(line) && unicode.IsDigit(rune(line[x])) {
					numStr += string(line[x])
					positions = append(positions, [2]int{x, y})
					x++
				}
				value, _ := strconv.Atoi(numStr)
				numbers = append(numbers, Token{value: value, positions: positions})
			} else if ch != '.' {
				// Any non-digit, non-period character is a symbol (including spaces)
				symbols[[2]int{x, y}] = true
				x++
			} else {
				x++
			}
		}
	}

	return numbers, symbols, width, height
}

func getAdjacentPositions(pos [2]int, width, height int) [][2]int {
	deltas := []struct{ dx, dy int }{
		{-1, -1}, {0, -1}, {1, -1},
		{-1, 0}, {1, 0},
		{-1, 1}, {0, 1}, {1, 1},
	}
	var positions [][2]int
	for _, delta := range deltas {
		newX := pos[0] + delta.dx
		newY := pos[1] + delta.dy
		if newX >= 0 && newX < width && newY >= 0 && newY < height {
			positions = append(positions, [2]int{newX, newY})
		}
	}
	return positions
}

func hasAdjacentSymbol(pos [2]int, symbolPositions map[[2]int]bool, width, height int) bool {
	for _, adj := range getAdjacentPositions(pos, width, height) {
		if symbolPositions[adj] {
			return true
		}
	}
	return false
}

func part1Soln(lines []string) int {
	numbers, symbols, width, height := parseGrid(lines)
	sum := 0

	symbolPositions := make(map[[2]int]bool)
	for pos := range symbols {
		symbolPositions[pos] = true
	}

	for _, number := range numbers {
		isPartNumber := false
		for _, pos := range number.positions {
			if hasAdjacentSymbol(pos, symbolPositions, width, height) {
				isPartNumber = true
				break
			}
		}
		if isPartNumber {
			sum += number.value
		}
	}

	return sum
}

func part2Soln(lines []string) int {
	numbers, symbols, width, height := parseGrid(lines)
	sum := 0

	positionToNumber := make(map[[2]int]int)
	for _, number := range numbers {
		for _, pos := range number.positions {
			positionToNumber[pos] = number.value
		}
	}

	digitToNumber := make(map[[2]int]int)
	for _, number := range numbers {
		for _, pos := range number.positions {
			digitToNumber[pos] = number.value
		}
	}

	getCharAt := func(lines []string, x, y int) rune {
		if y >= 0 && y < len(lines) && x >= 0 && x < len(lines[y]) {
			return rune(lines[y][x])
		}
		return ' '
	}

	for pos := range symbols {
		if getCharAt(lines, pos[0], pos[1]) != '*' {
			continue
		}
		adjacentNumbers := make(map[int]bool)
		for _, adj := range getAdjacentPositions(pos, width, height) {
			if val, ok := digitToNumber[adj]; ok {
				adjacentNumbers[val] = true
			}
		}
		if len(adjacentNumbers) == 2 {
			product := 1
			for val := range adjacentNumbers {
				product *= val
			}
			sum += product
		}
	}

	return sum
}

func main() {
	lines, _ := utils.ReadFileLines("/home/virtualdom/projects/leet-code/advent_of_code/2023/day_3/day_3.txt")

	part1 := part1Soln(lines)
	part2 := part2Soln(lines)

	fmt.Printf("Part 1: %d\n", part1) // 514969
	fmt.Printf("Part 2: %d\n", part2) // 78915902
}
