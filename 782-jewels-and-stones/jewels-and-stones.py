class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for j in stones:
            if j in jewels:
                count += 1

        return count