class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        idx = {}
        for i, c in enumerate(s):
            idx[c] = i
        diff = 0
        for i, c in enumerate(t):
            diff += abs(i - idx[c])
        return diff
        