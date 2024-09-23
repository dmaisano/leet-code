import pytest
from algorithms.move_zeroes import Solution


def test_move_zeroes() -> None:
    solution = Solution()

    # Test case 1: General case with zeros and non-zero numbers
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0], f"Expected [1, 3, 12, 0, 0] but got {nums}"

    # Test case 2: List with no zeros
    nums = [1, 2, 3, 4, 5]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5] but got {nums}"

    # Test case 3: List with only zeros
    nums = [0, 0, 0]
    solution.moveZeroes(nums)
    assert nums == [0, 0, 0], f"Expected [0, 0, 0] but got {nums}"

    # Test case 4: List with one element (zero)
    nums = [0]
    solution.moveZeroes(nums)
    assert nums == [0], f"Expected [0] but got {nums}"

    # Test case 5: List with one element (non-zero)
    nums = [5]
    solution.moveZeroes(nums)
    assert nums == [5], f"Expected [5] but got {nums}"

    # Test case 6: Empty list
    nums = []
    solution.moveZeroes(nums)
    assert nums == [], f"Expected [] but got {nums}"

    # Test case 7: Multiple zeros in between
    nums = [0, 0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0, 0], f"Expected [1, 3, 12, 0, 0, 0] but got {nums}"

    # Test case 8: Zeros at the beginning
    nums = [0, 0, 0, 1, 2]
    solution.moveZeroes(nums)
    assert nums == [1, 2, 0, 0, 0], f"Expected [1, 2, 0, 0, 0] but got {nums}"


if __name__ == "__main__":
    pytest.main()
