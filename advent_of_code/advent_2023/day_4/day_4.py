from advent_of_code.utils.read_file_lines import read_file_lines


class Soln:
    @staticmethod
    def solve_part_1(cards: list[str]) -> int:
        total_points = 0
        for line in cards:
            line = line.strip()
            if not line:
                continue
            # Remove the "Card X:" part by splitting on the colon.
            parts = line.split(":", 1)
            if len(parts) < 2:
                continue
            numbers_str = parts[1].strip()
            # Ensure that there's a vertical bar separating the two parts.
            if "|" not in numbers_str:
                continue
            left, right = numbers_str.split("|", 1)
            try:
                # Parse the winning numbers (left) and your numbers (right)
                winning_numbers = [int(num) for num in left.split()]
                your_numbers = [int(num) for num in right.split()]
            except ValueError:
                continue

            # Count how many of the numbers you have appear in the winning numbers.
            matches = len(set(winning_numbers) & set(your_numbers))
            # Calculate card points: first match gives 1 point, then each subsequent match doubles the points.
            card_points = 2 ** (matches - 1) if matches > 0 else 0
            total_points += card_points
        return total_points

    @staticmethod
    def solve_part_2(cards: list[str]) -> int:
        """
        For Part 2 we determine, for each card, the number of matching numbers.
        Each card (original or copy) wins additional copies as follows:
          - If a card has m matching numbers, then from the card immediately after it,
            you win one copy of the next m cards (or as many as remain).
        We simulate this propagation using a DP-style forward accumulation.
        """
        # Precompute the match count for each card.
        match_counts = []
        for line in cards:
            line = line.strip()
            if not line:
                match_counts.append(0)
                continue
            parts = line.split(":", 1)
            if len(parts) < 2:
                match_counts.append(0)
                continue
            numbers_str = parts[1].strip()
            if "|" not in numbers_str:
                match_counts.append(0)
                continue
            left, right = numbers_str.split("|", 1)
            try:
                winning_numbers = [int(num) for num in left.split()]
                your_numbers = [int(num) for num in right.split()]
            except ValueError:
                match_counts.append(0)
                continue
            matches = len(set(winning_numbers) & set(your_numbers))
            match_counts.append(matches)

        n = len(match_counts)
        # dp[i] holds the total number of instances (original and won copies) of card i.
        dp = [1] * n  # each card starts with one original copy.
        # Process each card in order.
        for i in range(n):
            m = match_counts[i]
            # A card wins copies of the next m cards (if available)
            end = min(n, i + m + 1)
            for j in range(i + 1, end):
                dp[j] += dp[i]
        return sum(dp)


if __name__ == "__main__":
    cards = read_file_lines("advent_of_code/advent_2023/day_4/day_4.txt")
    print(f"Total points: {Soln.solve_part_1(cards)}")
    print(f"Total scratchcards: {Soln.solve_part_2(cards)}")
