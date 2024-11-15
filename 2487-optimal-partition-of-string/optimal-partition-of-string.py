class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        cur = ''

        for i in range(len(s)):
            if s[i] in cur:
                ans += 1
                print(cur)
                cur = s[i]
            else:
                cur += s[i]  

        return ans