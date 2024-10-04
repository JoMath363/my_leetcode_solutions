class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = nums1 + nums2
        nums.sort()
        mid = len(nums) // 2
        print(nums)

        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            print(nums[mid], nums[mid - 1])
            sumMid = nums[mid] + nums[mid - 1]
            return sumMid / 2.0
        