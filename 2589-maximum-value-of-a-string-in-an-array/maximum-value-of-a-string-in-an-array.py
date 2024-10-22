class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
    
        maxVal = 0
        for s in strs:
            val = int(s) if s.isdigit() else len(s)
            maxVal = max(maxVal, val)
        return maxVal
        