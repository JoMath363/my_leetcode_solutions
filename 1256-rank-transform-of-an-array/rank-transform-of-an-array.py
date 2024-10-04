class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        nums = sorted({*arr})

        for i, n in enumerate(nums):
            ranks[n] = i + 1

        return [ranks[n] for n in arr]