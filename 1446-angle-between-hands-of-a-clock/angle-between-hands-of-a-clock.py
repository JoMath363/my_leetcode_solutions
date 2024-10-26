class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        M = minutes * 6
        H = (hour % 12) * 30 + (minutes / 60) * 30

        return min(abs(H - M), 360 - abs(H - M))