class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        D = defaultdict(int)
        res= []

        for n in nums:
            D[n] += 1

            if D[n] > 1:
                res.append(n)

        return res
                
        