class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = sorted(strs)
        first = words[0]
        last = words[-1]
        res = ''

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res
            