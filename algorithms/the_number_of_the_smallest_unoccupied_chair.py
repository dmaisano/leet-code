import heapq
import sys
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for i, (arr, dep) in enumerate(times):
            events.append((arr, 1, i))  # Arrival event, event_type=1
            events.append((dep, 0, i))  # Departure event, event_type=0

        # Sort events by time; departures before arrivals when times are equal
        events.sort()

        available_chairs: List[int] = []
        next_chair = 0
        friend_to_chair: dict[int, int] = {}

        for time, event_type, friend_index in events:
            if event_type == 0:  # Departure
                chair = friend_to_chair[friend_index]
                heapq.heappush(available_chairs, chair)
            else:  # Arrival
                if available_chairs:
                    chair = heapq.heappop(available_chairs)
                else:
                    chair = next_chair
                    next_chair += 1
                friend_to_chair[friend_index] = chair
                if friend_index == targetFriend:
                    return chair

        return sys.maxsize
