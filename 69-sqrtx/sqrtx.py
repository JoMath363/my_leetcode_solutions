class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1

        while num * num < x:
            num += 1

        if num * num != x:
            return num - 1 
        return num