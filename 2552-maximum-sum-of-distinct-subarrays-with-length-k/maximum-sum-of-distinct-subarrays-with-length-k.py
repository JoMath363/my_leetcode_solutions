class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        cur = 0
        nSet = set()
        l = 0
        
        for r in range(len(nums)):
            while nums[r] in nSet or r - l + 1 > k:
                nSet.remove(nums[l])
                cur -= nums[l]
                l += 1
            
            nSet.add(nums[r])
            cur += nums[r]

            if r - l + 1 == k:
                max_sum = max(max_sum, cur)
        
        return max_sum
