class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        d = defaultdict(int)
        lonely = []
        
        for n in nums:
            d[n] += 1

        for n in nums:
            if d[n] == 1 and not d[n-1] and not d[n+1]:
                lonely.append(n)

        return lonely