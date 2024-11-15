class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        counter = 0
        res = ''

        for i in range(len(s)):
            counter += 1
            if i == len(s) - 1 or s[i] != s[i + 1]:
                res += f'{counter}{s[i]}'
                counter = 0

        return res

