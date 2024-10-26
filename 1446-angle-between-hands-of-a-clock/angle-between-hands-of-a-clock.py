class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        M = minutes / 60 * 360
        H = (minutes / 60 * 30)
        if not hour == 12:
            H += (hour / 12 * 360)

        print(M, H)
        ans = abs(H - M)
        if ans > 180:
            return 360 - ans
        return ans