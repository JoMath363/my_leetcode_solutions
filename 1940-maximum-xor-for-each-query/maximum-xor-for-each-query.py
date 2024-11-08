class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []

        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            res.append(nums[i] ^ (2 ** maximumBit - 1))

        return res