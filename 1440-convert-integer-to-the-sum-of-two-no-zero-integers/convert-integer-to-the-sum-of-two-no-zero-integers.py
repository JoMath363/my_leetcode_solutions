class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        for x in range(1, n):
            diff = n - x
            if not ('0' in str(diff) or '0' in str(x)):
                return [x, diff]

