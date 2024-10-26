class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        H = (minutes / 60 * 30)
        if not hour == 12:
            H += (hour / 12 * 360)

        ans = abs(H - minutes / 60 * 360)
        
        if ans > 180:
            return 360 - ans
        return ans