class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)

        for _ in range(n):
            for i in range(n - 1):
                if not nums[i + 1] < nums[i]:
                    continue
                
                if bin(nums[i]).count('1') == bin(nums[i + 1]).count('1'):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums == sorted(nums)
