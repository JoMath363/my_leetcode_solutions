class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        ans = 0
        for i in range(len(arr)):
            total = (i + 1) * (len(arr) - i)
            ans = ans + (total // 2 + total % 2) * arr[i]
        return ans

        