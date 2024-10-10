class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        timeList = []

        for c in customers:
            [arrival, time] = c
            current = max(current, arrival) + time

            timeList.append(current - arrival)
            
        return sum(timeList) / len(timeList)

