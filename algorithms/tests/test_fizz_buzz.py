import pytest

from algorithms.fizz_buzz import Solution


def test_fizzbuzz_with_n_3() -> None:
    sol = Solution()
    assert sol.fizzBuzz(3) == ["1", "2", "Fizz"]


def test_fizzbuzz_with_n_5() -> None:
    sol = Solution()
    assert sol.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fizzbuzz_with_n_15() -> None:
    sol = Solution()
    assert sol.fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_fizzbuzz_with_n_1() -> None:
    sol = Solution()
    assert sol.fizzBuzz(1) == ["1"]


def test_fizzbuzz_with_n_10() -> None:
    sol = Solution()
    assert sol.fizzBuzz(10) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
    ]


def test_fizzbuzz_with_n_30() -> None:
    sol = Solution()
    assert sol.fizzBuzz(30) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
        "16",
        "17",
        "Fizz",
        "19",
        "Buzz",
        "Fizz",
        "22",
        "23",
        "Fizz",
        "Buzz",
        "26",
        "Fizz",
        "28",
        "29",
        "FizzBuzz",
    ]


if __name__ == "__main__":
    pytest.main()
