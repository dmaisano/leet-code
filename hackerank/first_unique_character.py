from collections import Counter


def getUniqueCharacter(s: str) -> int:
    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Iterate over the string to find the first unique character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index + 1  # Return 1-based index

    return -1  # If no unique character is found
