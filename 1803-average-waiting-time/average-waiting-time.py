class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        total = 0

        for c in customers:
            [arrival, time] = c
            current = max(current, arrival) + time

            total += current - arrival

        return total / len(customers)

