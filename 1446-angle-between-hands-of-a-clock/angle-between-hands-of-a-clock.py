class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        M = minutes * 6
        H = (hour % 12) * 30 + (minutes / 60) * 30

        if H > M:
            _sum = H - M
            return min(_sum, 360 - _sum)
        _sum = M - H
        return min(_sum, 360 - _sum)