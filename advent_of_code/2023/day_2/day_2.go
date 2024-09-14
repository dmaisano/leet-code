package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/dmaisano/leet-code/utils"
)

type Counts struct {
	Red   int
	Green int
	Blue  int
}

type Game struct {
	ID     int
	Counts []Counts
}

func parseGame(line string) Game {
	parts := strings.Split(line, ": ")
	idPart, countParts := parts[0], strings.Split(parts[1], "; ")
	counts := []Counts{}

	for _, countPart := range countParts {
		colors := map[string]int{"red": 0, "green": 0, "blue": 0}
		part := strings.Split(countPart, ", ")

		for _, colorPart := range part {
			colorInfo := strings.Split(colorPart, " ")
			count, _ := strconv.Atoi(colorInfo[0])
			colors[colorInfo[1]] = count
		}

		counts = append(counts, Counts{Red: colors["red"], Green: colors["green"], Blue: colors["blue"]})
	}

	id, _ := strconv.Atoi(strings.TrimPrefix(idPart, "Game "))
	return Game{ID: id, Counts: counts}
}

func isGamePossible(game Game, maxCounts Counts) bool {
	for _, counts := range game.Counts {
		if counts.Red > maxCounts.Red || counts.Green > maxCounts.Green || counts.Blue > maxCounts.Blue {
			return false
		}
	}
	return true
}

func part1Soln(lines []string) int {
	redCount, greenCount, blueCount := 12, 13, 14
	possibleGameIDs := []int{}

	for i, line := range lines {
		parsedGame := parseGame(line)
		if isGamePossible(parsedGame, Counts{Red: redCount, Green: greenCount, Blue: blueCount}) {
			possibleGameIDs = append(possibleGameIDs, i+1)
		}
	}

	sum := 0
	for _, id := range possibleGameIDs {
		sum += id
	}
	return sum
}

func findMinimumCubes(game Game) Counts {
	minCubes := Counts{}
	for _, counts := range game.Counts {
		minCubes.Red = max(counts.Red, minCubes.Red)
		minCubes.Green = max(counts.Green, minCubes.Green)
		minCubes.Blue = max(counts.Blue, minCubes.Blue)
	}
	return minCubes
}

func calcCubePower(count Counts) int {
	return count.Red * count.Green * count.Blue
}

func part2Soln(lines []string) int {
	sumCubePowers := 0
	for _, line := range lines {
		parsedGame := parseGame(line)
		minCubes := findMinimumCubes(parsedGame)
		sumCubePowers += calcCubePower(minCubes)
	}
	return sumCubePowers
}

func main() {
	lines, _ := utils.ReadFileLines("/home/virtualdom/projects/leet-code/advent_of_code/2023/day_2/day_2.txt")

	sumGameIds := part1Soln(lines)
	sumCubePowers := part2Soln(lines)

	fmt.Printf("part 1 total points: %d\n", sumGameIds)
	fmt.Printf("Part 2 total points: %d\n", sumCubePowers)
}
