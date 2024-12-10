class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            if i % 2 == 1:
                n = ord(s[i - 1]) - 97 + int(s[i])
            
                if n > 25:
                    n -= 26

                res += chr(n + 97)
            else:
                res += s[i]
                
        return res
                       