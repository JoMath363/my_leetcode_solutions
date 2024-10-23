class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        less, equal, more = [], [], []
        
        for n in nums:
            if n == pivot:
                equal.append(n)
            elif n < pivot:
                less.append(n)
            else:
                more.append(n)

        return less + equal + more

        