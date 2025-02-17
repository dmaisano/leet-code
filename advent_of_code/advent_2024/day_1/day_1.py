from collections import Counter
from advent_of_code.utils.read_file_lines import read_file_lines


class Soln:
    @staticmethod
    def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
        """
        Parses the input lines into two lists of integers.
        Each line is expected to have two integers separated by whitespace.
        Returns a tuple of (left_numbers, right_numbers).
        """
        left, right = [], []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            left.append(int(parts[0]))
            right.append(int(parts[1]))
        return left, right

    @staticmethod
    def solve_part1(lines: list[str]) -> int:
        """
        Part One:
        Given two lists of integers (left and right), sort each list independently.
        Pair up:
          - the smallest left number with the smallest right number,
          - the second smallest left with the second smallest right, and so on.
        Then, sum the absolute differences between each pair.
        """
        left, right = Soln.parse_input(lines)
        left_sorted = sorted(left)
        right_sorted = sorted(right)
        total_distance = 0
        for l, r in zip(left_sorted, right_sorted):
            total_distance += abs(l - r)
        return total_distance

    @staticmethod
    def solve_part2(lines: list[str]) -> int:
        """
        Part Two:
        For each number in the left list, count how many times it appears in the right list.
        Multiply the left number by its occurrence count and sum all such products for the similarity score.
        """
        left, right = Soln.parse_input(lines)
        right_counter = Counter(right)
        similarity_score = 0
        for num in left:
            similarity_score += num * right_counter.get(num, 0)
        return similarity_score


if __name__ == "__main__":
    lines = read_file_lines("advent_of_code/advent_2024/day_1/day_1.txt")
    print("Part 1:", Soln.solve_part1(lines))
    print("Part 2:", Soln.solve_part2(lines))
