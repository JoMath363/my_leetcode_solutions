class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''

        for i in range(len(s) - 2):
            if s[i] == s[i+1]== s[i+2]:
                continue

            ans += s[i]

        return ans + s[-2:]

