from typing import List, Dict, Tuple
from advent_of_code.utils.read_file_lines import read_file_lines


class Soln:
    @staticmethod
    def _apply_mapping(val: int, rules: List[Tuple[int, int, int]]) -> int:
        """
        Given a value and a list of mapping rules (each defined as a tuple:
        (dest_start, src_start, range_length)), return the mapped value.
        If the value lies in a rule's source range [src_start, src_start+range_length),
        then the mapped value is dest_start + (val - src_start). If none of the rules
        apply, the mapping is the identity.
        """
        for dest_start, src_start, length in rules:
            if src_start <= val < src_start + length:
                return dest_start + (val - src_start)
        return val

    @staticmethod
    def _part_1_parse_input(
        lines: List[str],
    ) -> Tuple[List[int], Dict[str, List[Tuple[int, int, int]]]]:
        """
        Parses the input file lines. It expects the first nonblank line starting
        with "seeds:" to list the initial seed numbers. Then, for every mapping block
        (lines ending with "map:"), it reads subsequent lines containing three numbers
        (destination start, source start, and range length) and stores them as mapping rules.
        """
        seeds: List[int] = []
        maps: Dict[str, List[Tuple[int, int, int]]] = {}
        current_map = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("seeds:"):
                # Parse the initial seed numbers.
                seeds = list(map(int, line[len("seeds:") :].strip().split()))
            elif "map:" in line:
                # New mapping block; extract the key (for example "seed-to-soil")
                header = line.split("map:")[0].strip()
                current_map = header
                maps[current_map] = []
            else:
                # Read a mapping line (three integers)
                if current_map is not None:
                    parts = line.split()
                    if len(parts) == 3:
                        dest_start, src_start, length = map(int, parts)
                        maps[current_map].append((dest_start, src_start, length))
        return seeds, maps

    @staticmethod
    def solve_part_1(lines: List[str]) -> int:
        """
        Processes the almanac in the input file and returns the lowest location number that
        corresponds to any of the initial seed numbers. The conversion chain is as follows:

           seed --(seed-to-soil)--> soil --(soil-to-fertilizer)--> fertilizer
                --(fertilizer-to-water)--> water --(water-to-light)--> light
                --(light-to-temperature)--> temperature --(temperature-to-humidity)--> humidity
                --(humidity-to-location)--> location

        For each conversion, if the current number lies in any mapped range then it is converted;
        otherwise it is left unchanged.
        """
        seeds, maps = Soln._part_1_parse_input(lines)
        conversion_order = [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]
        location_numbers: List[int] = []
        for seed in seeds:
            value: int = seed
            for key in conversion_order:
                rules = maps.get(key, [])
                value = Soln._apply_mapping(value, rules)
            location_numbers.append(value)
        return min(location_numbers)

    @staticmethod
    def _part_2_parse_input(
        lines: List[str],
    ) -> Tuple[List[Tuple[int, int]], Dict[str, List[Tuple[int, int, int]]]]:
        """
        For Part 2, the 'seeds:' line describes pairs of numbers.
        Each pair (s, l) represents a range: seeds s, s+1, …, s+l-1.
        """
        seed_ranges: List[Tuple[int, int]] = []
        maps: Dict[str, List[Tuple[int, int, int]]] = {}
        current_map = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("seeds:"):
                nums = list(map(int, line[len("seeds:") :].strip().split()))
                # Interpret the list in pairs.
                for i in range(0, len(nums), 2):
                    start = nums[i]
                    length = nums[i + 1]
                    seed_ranges.append((start, start + length))
            elif "map:" in line:
                header = line.split("map:")[0].strip()
                current_map = header
                maps[current_map] = []
            else:
                if current_map is not None:
                    parts = line.split()
                    if len(parts) == 3:
                        dest_start, src_start, length = map(int, parts)
                        maps[current_map].append((dest_start, src_start, length))
        return seed_ranges, maps

    @staticmethod
    def _apply_mapping_stage(
        intervals: List[Tuple[int, int, int]],
        rules: List[Tuple[int, int, int]],
    ) -> List[Tuple[int, int, int]]:
        """
        Given a piecewise function represented by intervals (a, b, off) where f(x)=x+off for x in [a,b),
        apply a mapping stage defined by 'rules' (each (dest_start, src_start, length)) in order.
        If for a value f(x) is in [src_start, src_start+length), then that part is remapped to:
            f(x) = x + off + (dest_start - src_start)
        Only the first rule that applies is used.
        """
        new_intervals: List[Tuple[int, int, int]] = []
        for a, b, off in intervals:
            # Start with the entire interval unmapped.
            unmapped = [(a, b)]
            for dest_start, src_start, length in rules:
                updated_unmapped = []
                for s, e in unmapped:
                    # Compute where the rule applies in terms of x.
                    rule_low = src_start - off
                    rule_high = src_start + length - off
                    inter_s = max(s, rule_low)
                    inter_e = min(e, rule_high)
                    if inter_s < inter_e:
                        # For x in [inter_s, inter_e) the rule applies.
                        new_intervals.append(
                            (inter_s, inter_e, off + (dest_start - src_start))
                        )
                        # Keep the portions that do not match the rule.
                        if s < inter_s:
                            updated_unmapped.append((s, inter_s))
                        if inter_e < e:
                            updated_unmapped.append((inter_e, e))
                    else:
                        updated_unmapped.append((s, e))
                unmapped = updated_unmapped
            # Any x that did not match any rule remains unchanged.
            for s, e in unmapped:
                new_intervals.append((s, e, off))
        return new_intervals

    @staticmethod
    def solve_part_2(lines: List[str]) -> int:
        """
        Processes the almanac for Part 2. It obtains the seed ranges (each representing
        many seeds) and then applies the conversion chain as a piecewise function.
        Since each stage is an affine function (with slope 1), the minimum over an interval
        [a,b) (where F(x)= x+offset) occurs at x = a. We return the minimum value found.
        """
        seed_ranges, maps = Soln._part_2_parse_input(lines)
        # Represent each seed range as an interval: (start, end, offset=0)
        intervals: List[Tuple[int, int, int]] = []
        for start, end in seed_ranges:
            intervals.append((start, end, 0))
        conversion_order = [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]
        for key in conversion_order:
            rules = maps.get(key, [])
            intervals = Soln._apply_mapping_stage(intervals, rules)
        # On each interval, since F(x)= x+offset is strictly increasing,
        # the minimum is achieved at the left endpoint.
        best = min(s + off for s, _, off in intervals)
        return best


if __name__ == "__main__":
    lines = read_file_lines("advent_of_code/advent_2023/day_5/day_5.txt")
    print(f"Lowest location (Part 1): {Soln.solve_part_1(lines)}")
    print(f"Lowest location (Part 2): {Soln.solve_part_2(lines)}")
