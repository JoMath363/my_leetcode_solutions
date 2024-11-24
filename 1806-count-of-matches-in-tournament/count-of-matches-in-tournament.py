class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n > 1:
            if n % 2 == 0:
                matches += ceil(n / 2)
                n = ceil(n / 2)
            else:
                matches += ceil((n - 1) / 2)
                n = ceil((n - 1) / 2 + 1)

        return matches
                