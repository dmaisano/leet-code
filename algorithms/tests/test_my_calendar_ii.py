import pytest
from algorithms.my_calendar_ii import MyCalendarTwo


def test_booking_successful() -> None:
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) == True
    assert calendar.book(50, 60) == True
    assert calendar.book(10, 40) == True
    assert calendar.book(5, 10) == True
    assert calendar.book(25, 55) == True


def test_booking_fails_on_triple_booking() -> None:
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) == True
    assert calendar.book(10, 40) == True
    assert calendar.book(5, 15) == False
    assert calendar.book(5, 10) == True


def test_mixed_bookings() -> None:
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) == True
    assert calendar.book(50, 60) == True
    assert calendar.book(10, 40) == True
    assert calendar.book(5, 15) == False
    assert calendar.book(20, 30) == True
    assert calendar.book(30, 40) == True
    assert calendar.book(60, 70) == True


def test_edge_case_no_overlap() -> None:
    calendar = MyCalendarTwo()
    assert calendar.book(1, 5) == True
    assert calendar.book(5, 10) == True
    assert calendar.book(10, 15) == True


def test_edge_case_exact_overlap() -> None:
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) == True
    assert calendar.book(10, 20) == True
    assert calendar.book(10, 20) == False


if __name__ == "__main__":
    pytest.main()
