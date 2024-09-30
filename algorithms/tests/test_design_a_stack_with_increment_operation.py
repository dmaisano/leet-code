import pytest
from algorithms.design_a_stack_with_increment_operation import CustomStack


def test_push() -> None:
    stk = CustomStack(3)
    stk.push(1)
    stk.push(2)
    assert stk.stack == [1, 2]

    stk.push(3)
    assert stk.stack == [1, 2, 3]

    stk.push(4)
    assert stk.stack == [1, 2, 3]


def test_pop() -> None:
    stk = CustomStack(3)
    stk.push(1)
    stk.push(2)
    stk.push(3)

    assert stk.pop() == 3
    assert stk.stack == [1, 2]

    assert stk.pop() == 2
    assert stk.stack == [1]

    assert stk.pop() == 1
    assert stk.stack == []

    assert stk.pop() == -1


def test_increment() -> None:
    stk = CustomStack(3)
    stk.push(1)
    stk.push(2)
    stk.push(3)

    stk.increment(2, 100)
    assert stk.stack == [101, 102, 3]

    stk.increment(5, 50)
    assert stk.stack == [151, 152, 53]


def test_combined_operations() -> None:
    stk = CustomStack(3)

    stk.push(1)
    stk.push(2)
    assert stk.stack == [1, 2]

    assert stk.pop() == 2
    assert stk.stack == [1]

    stk.push(2)
    stk.push(3)
    assert stk.stack == [1, 2, 3]

    stk.push(4)
    assert stk.stack == [1, 2, 3]

    stk.increment(5, 100)
    assert stk.stack == [101, 102, 103]

    stk.increment(2, 100)
    assert stk.stack == [201, 202, 103]

    assert stk.pop() == 103
    assert stk.pop() == 202
    assert stk.pop() == 201
    assert stk.pop() == -1


if __name__ == "__main__":
    pytest.main()
