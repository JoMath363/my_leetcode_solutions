class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 0, n

        while l <= r:
            mid = l + (r - l) // 2
            k = mid * (mid + 1) // 2

            if k == n:
                return mid
            elif k < n:
                l = mid + 1
            else:
                r = mid - 1
        return r

        