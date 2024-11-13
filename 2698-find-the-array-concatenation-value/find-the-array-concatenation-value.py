class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if i < j:
                n = int(str(nums[i]) + str(nums[j]))
                res += n
            else:
                res += nums[i]
            i += 1
            j -= 1
        return res