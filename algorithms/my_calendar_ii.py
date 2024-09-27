from typing import List, Tuple


class MyCalendarTwo:

    def __init__(self) -> None:
        self.bookings: List[Tuple[int, int]] = []  # List to store all single bookings
        self.overlaps: List[Tuple[int, int]] = []  # List to store all double bookings

    def book(self, start: int, end: int) -> bool:
        # Check if this event would cause a triple booking
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                return False

        # Add new overlaps if the event overlaps with any existing booking
        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:
                # Calculate the overlap and store it in overlaps
                overlap_start = max(start, booking_start)
                overlap_end = min(end, booking_end)
                self.overlaps.append((overlap_start, overlap_end))

        self.bookings.append((start, end))
        return True
