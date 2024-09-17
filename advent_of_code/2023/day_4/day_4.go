package main

import (
	"container/list"
	"fmt"
	"strconv"
	"strings"

	"github.com/dmaisano/leet-code/utils"
)

type Card struct {
	WinningNumbers []int
	YourNumbers    []int
}

func parseLines(lines []string) []Card {
	var cards []Card
	for _, line := range lines {
		cards = append(cards, parseCard(line))
	}
	return cards
}

func parseCard(line string) Card {
	parts := strings.Split(line, "|")

	return Card{
		WinningNumbers: parseNumbers(parts[0]),
		YourNumbers:    parseNumbers(parts[1]),
	}
}

func parseNumbers(s string) []int {
	fields := strings.Fields(s)
	numbers := make([]int, len(fields))
	for i, field := range fields {
		num, _ := strconv.Atoi(strings.TrimSpace(field))
		numbers[i] = num
	}
	return numbers
}

func part1Soln(lines []string) int {
	cards := parseLines(lines)

	calculatePoints := func(card Card) int {
		matchCount := 0

		winningSet := make(map[int]bool)
		for _, num := range card.WinningNumbers {
			winningSet[num] = true
		}

		for _, num := range card.YourNumbers {
			if winningSet[num] {
				matchCount++
			}
		}

		if matchCount == 0 {
			return 0
		}
		return 1 << (matchCount - 1) // 1 << (matchCount - 1) is 2^(matchCount-1)
	}

	totalPoints := 0
	for _, card := range cards {
		totalPoints += calculatePoints(card)
	}
	return totalPoints
}

func part2Soln(lines []string) int {
	cards := parseLines(lines)
	totalCards := len(cards)

	queue := list.New()

	for i := 0; i < len(cards); i++ {
		queue.PushBack(i)
	}

	countMatches := func(card Card) int {
		winNumbersSet := make(map[int]struct{})
		for _, num := range card.WinningNumbers {
			winNumbersSet[num] = struct{}{}
		}

		matches := 0
		for _, num := range card.YourNumbers {
			if _, exists := winNumbersSet[num]; exists {
				matches++
			}
		}
		return matches
	}

	for queue.Len() > 0 {
		element := queue.Front()
		queue.Remove(element)
		cardIndex := element.Value.(int)

		card := cards[cardIndex]

		numMatches := countMatches(card)

		for i := 1; i <= numMatches; i++ {
			nextCardIndex := cardIndex + i
			if nextCardIndex < len(cards) {
				queue.PushBack(nextCardIndex)
				totalCards++
			} else {
				break
			}
		}
	}

	return totalCards
}

func main() {
	lines, _ := utils.ReadFileLines("/home/virtualdom/projects/leet-code/advent_of_code/2023/day_4/day_4.txt")

	part1TotalCards := part1Soln(lines)
	part2TotalCards := part2Soln(lines)

	fmt.Printf("Part 1 points: %d\n", part1TotalCards)
	fmt.Printf("Part 2 total cards: %d\n", part2TotalCards)
}
