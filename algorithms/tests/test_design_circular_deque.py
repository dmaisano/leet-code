import pytest
from algorithms.design_circular_deque import MyCircularDeque


def test_insert_front() -> None:
    deque = MyCircularDeque(3)
    assert deque.insertFront(1) == True
    assert deque.insertFront(2) == True
    assert deque.insertFront(3) == True
    assert deque.insertFront(4) == False


def test_insert_last() -> None:
    deque = MyCircularDeque(3)
    assert deque.insertLast(1) == True
    assert deque.insertLast(2) == True
    assert deque.insertLast(3) == True
    assert deque.insertLast(4) == False


def test_delete_front() -> None:
    deque = MyCircularDeque(3)
    deque.insertFront(1)
    deque.insertFront(2)
    deque.insertFront(3)
    assert deque.deleteFront() == True
    assert deque.deleteFront() == True
    assert deque.deleteFront() == True
    assert deque.deleteFront() == False


def test_delete_last() -> None:
    deque = MyCircularDeque(3)
    deque.insertLast(1)
    deque.insertLast(2)
    deque.insertLast(3)
    assert deque.deleteLast() == True
    assert deque.deleteLast() == True
    assert deque.deleteLast() == True
    assert deque.deleteLast() == False


def test_get_front() -> None:
    deque = MyCircularDeque(3)
    assert deque.getFront() == -1
    deque.insertFront(1)
    assert deque.getFront() == 1
    deque.insertFront(2)
    assert deque.getFront() == 2


def test_get_rear() -> None:
    deque = MyCircularDeque(3)
    assert deque.getRear() == -1
    deque.insertLast(1)
    assert deque.getRear() == 1
    deque.insertLast(2)
    assert deque.getRear() == 2


def test_is_empty() -> None:
    deque = MyCircularDeque(3)
    assert deque.isEmpty() == True
    deque.insertFront(1)
    assert deque.isEmpty() == False
    deque.deleteFront()
    assert deque.isEmpty() == True


def test_is_full() -> None:
    deque = MyCircularDeque(3)
    assert deque.isFull() == False
    deque.insertLast(1)
    deque.insertLast(2)
    deque.insertLast(3)
    assert deque.isFull() == True
    deque.deleteLast()
    assert deque.isFull() == False


def test_complex_scenario() -> None:
    deque = MyCircularDeque(3)
    assert deque.insertLast(1) == True
    assert deque.insertLast(2) == True
    assert deque.insertFront(3) == True
    assert deque.insertFront(4) == False
    assert deque.getRear() == 2
    assert deque.isFull() == True
    assert deque.deleteLast() == True
    assert deque.insertFront(4) == True
    assert deque.getFront() == 4


if __name__ == "__main__":
    pytest.main()
