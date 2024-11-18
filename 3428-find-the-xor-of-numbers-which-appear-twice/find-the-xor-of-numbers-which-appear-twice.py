class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)

        for i in nums:
            mp[i] += 1

            if mp[i] == 2:
                res ^= i 

        return res



