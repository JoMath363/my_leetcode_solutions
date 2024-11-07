class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []

        for n in nums:
            x = 0
            for d in str(n):
                x += int(d)
            res.append(x)

        return min(res)
        