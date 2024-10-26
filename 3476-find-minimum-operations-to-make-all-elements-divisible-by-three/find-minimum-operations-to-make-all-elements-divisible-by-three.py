class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            if n % 3 == 1 or n % 3 == 2:
                ans += 1

        return ans
