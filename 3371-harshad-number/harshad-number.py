class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res = sum([int(n) for n in str(x)])

        return res if x % res == 0 else -1