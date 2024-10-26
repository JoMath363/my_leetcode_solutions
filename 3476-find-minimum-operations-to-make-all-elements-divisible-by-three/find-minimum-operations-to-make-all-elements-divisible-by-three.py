class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            if n % 3 == 0:
                continue
                
            if (n + 1) % 3 == 0 or (n - 1) % 3 == 0:
                ans += 1
            else:
                ans += 2

        return ans
