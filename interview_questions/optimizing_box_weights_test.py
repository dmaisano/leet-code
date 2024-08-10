import pytest
from .optimizing_box_weights import minimal_heaviest_setA


# Test case 1: Example with mixed weights from the problem statement
def test_mixed_weights_example_1() -> None:
    arr = [5, 3, 2, 4, 1, 2]
    expected_output = [4, 5]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 2: Example with mixed weights from the problem statement
def test_mixed_weights_example_2() -> None:
    arr = [4, 2, 5, 1, 6]
    expected_output = [5, 6]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 3: Single element in the array
def test_single_element_array() -> None:
    arr = [1]
    expected_output = [1]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 4: All elements are identical
def test_identical_elements_array() -> None:
    arr = [2, 2, 2, 2]
    expected_output = [2, 2]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 5: Verify that elements are returned in sorted order
def test_verify_ascending_order() -> None:
    arr = [1, 2, 4, 5, 3]
    expected_output = [4, 5]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 6: Already sorted array in descending order
def test_sorted_descending_order() -> None:
    arr = [5, 4, 3, 2, 1]
    expected_output = [4, 5]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 7: Array with large numbers
def test_large_numbers_array() -> None:
    arr = [100, 200, 300, 400]
    expected_output = [400]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 8: Array with minimal size containing two elements
def test_two_element_array() -> None:
    arr = [1, 2]
    expected_output = [2]
    assert minimal_heaviest_setA(arr) == expected_output


# Test case 9: Array with random order of weights
def test_random_order_array() -> None:
    arr = [3, 1, 4, 2, 5]
    expected_output = [5]
    assert minimal_heaviest_setA(arr)
