class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        for i in range(1, n):
            inverted = ''
            for j in range(len(s) - 1, -1, -1):
                inverted += '1' if s[j] == '0' else '0'

            s += '1' + inverted

        return s[k-1]