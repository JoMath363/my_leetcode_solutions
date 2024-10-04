class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = []
        white = []
        blue = []

        for n in nums:
            if n == 0:
                red.append(n)
            elif n == 1:
                white.append(n)
            else:
                blue.append(n)

        nums.clear()
        nums += (red + white + blue)
            