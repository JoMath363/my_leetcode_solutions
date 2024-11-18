class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for i in nums:
            mp[i] += 1

            if mp[i] > (len(nums) // 2):
                return i