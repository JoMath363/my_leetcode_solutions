class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        ans = 0
        for i in s:
            if i not in d:
                d.add(i)
            else:
                ans += 1
                d = set(i)
        return ans + 1 if len(d) else ans