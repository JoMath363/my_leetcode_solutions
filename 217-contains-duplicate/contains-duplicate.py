class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len({*nums}) < len(nums)
