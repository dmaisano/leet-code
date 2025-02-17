from math import prod
from advent_of_code.utils.read_file_lines import read_file_lines
import re
from typing import Dict, Set, Tuple, TypeAlias

re_symbol = r"[^.\d]"
re_digit = r"\d+"
re_gear = r"\*"
SymbolAdjacent: TypeAlias = Set[Tuple[int, int]]


class Soln:
    @staticmethod
    def find_adjacent_indices(lines: list[str]) -> SymbolAdjacent:
        symbol_adjacent: SymbolAdjacent = set()
        for row, line in enumerate(lines):
            for sym in re.finditer(re_symbol, line):
                col = sym.start()
                symbol_adjacent |= set(
                    (r, c)
                    for r in range(row - 1, row + 2)
                    for c in range(col - 1, col + 2)
                )
        return symbol_adjacent

    @staticmethod
    def solve_part_1(
        lines: list[str],
    ) -> list[int]:
        symbol_adjacent = Soln.find_adjacent_indices(lines)
        part_numbers: list[int] = []
        for row, line in enumerate(lines):
            for num in re.finditer(re_digit, line):
                if any((row, col) in symbol_adjacent for col in range(*num.span())):
                    part_numbers.append(int(num.group()))
        return part_numbers

    @staticmethod
    def find_gear_indices(lines: list[str]) -> dict[tuple[int, int], set[int]]:
        gears: Dict[tuple[int, int], set[int]] = {}
        for row, line in enumerate(lines):
            for sym in re.finditer(re_symbol, line):
                col = sym.start()
                gears[(row, col)] = set()
        return gears

    @staticmethod
    def fill_gears(
        lines: list[str], gears: dict[tuple[int, int], set[int]]
    ) -> dict[tuple[int, int], set[int]]:
        for row, line in enumerate(lines):
            for num in re.finditer(re_digit, line):
                for r in range(row - 1, row + 2):
                    for c in range(num.start() - 1, num.end() + 1):
                        if (r, c) in gears:
                            gears[(r, c)].add(int(num.group()))
        return gears

    @staticmethod
    def solve_part_2(lines: list[str]) -> int:
        gears = Soln.find_gear_indices(lines)
        gears = Soln.fill_gears(lines, gears)
        total = 0
        for _, nums in gears.items():
            if len(nums) == 2:
                total += prod(nums)
        return total


if __name__ == "__main__":
    lines = read_file_lines("advent_of_code/advent_2023/day_3/day_3.txt")
    print(
        f"(Part 1) The sum of all part numbers in the engine schematic is: {sum(Soln.solve_part_1(lines))}"
    )
    print(f"(Part 2) The gear ratios product is: {Soln.solve_part_2(lines)}")
