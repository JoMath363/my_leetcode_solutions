class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            for j in range(i + 1, i + k):
                if nums[j] < nums[j-1] or not nums[j] == nums[j - 1] + 1:
                    res.append(-1)
                    break

            if len(res) < i + 1:
                res.append(max(nums[i:i + k]))

        return res

