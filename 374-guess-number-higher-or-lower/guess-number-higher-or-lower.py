# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l, r = 0, n

        while l <= r:
            mid = (r + l) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res > 0:
                l = mid + 1
            else:
                r = mid - 1
        return -1