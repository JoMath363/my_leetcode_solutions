class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter:
            if counter[i] > 2:
                return False
        return True