class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        for char in s:
            if len(res) < 2 or res[-1] != char or res[-2] != char:
                res += char
        return res

