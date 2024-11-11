class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert_cnt = 0
        length = (1 << n) - 1

        while k > 1:
            if k == length // 2 + 1:
                return "1" if invert_cnt % 2 == 0 else "0"

            if k > length // 2:
                k = length + 1 - k
                invert_cnt += 1

            length //= 2
        
        return "0" if invert_cnt % 2 == 0 else "1"