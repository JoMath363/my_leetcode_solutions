class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        nums.insert(0, 0)
        
        self.nums = nums

        print(nums)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return self.nums[right + 1] - self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)