class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        size = len(nums)

        left = [1] * size
        right = [1] * size
        products = [1] * size

        for i in range(1, size):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(size - 2, -1, -1):
            right[i] = nums[i+1] * right[i+1]

        for i in range(size):
            products[i] = right[i] * left[i]

        return products
        
        