class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long1, long0 = 0, 0
        cur1, cur0 = 0, 0

        for i in s:
            if i == '1':
                cur0 = 0
                cur1 += 1
                long1 = max(long1, cur1)
            else:
                cur1 = 0
                cur0 += 1
                long0 = max(long0, cur0)

        return long1 > long0
