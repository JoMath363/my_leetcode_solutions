class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = i
            tMap[t[i]] = i

        diff = 0
        for char in s:
            diff += abs(sMap[char] - tMap[char])

        return diff
        