class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sMap, tMap = {}, {}
        diff = 0
        
        for i in range(len(s)):
            sMap[s[i]] = i
            tMap[t[i]] = i
        
        for char in s:
            diff += abs(sMap[char] - tMap[char])

        return diff
        