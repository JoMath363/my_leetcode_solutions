class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            if i % 2 == 1:
                res += chr(ord(s[i - 1]) + int(s[i]))
            else:
                res += s[i]
                
        return res
                       