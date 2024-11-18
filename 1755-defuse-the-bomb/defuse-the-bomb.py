class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        ans = []
        nums = code * 3
        for i in range(n, n * 2):
            if k > 0:
                ans.append(sum(nums[i + 1 : i + k + 1]))
            else:
                ans.append(sum(nums[i + k : i]))
        return ans