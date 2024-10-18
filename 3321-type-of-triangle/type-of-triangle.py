class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        [a, b, c] = nums

        if not (a + b > c and b + c > a and c + a > b):
            return 'none'
        elif a == b == c:
            return 'equilateral'
        elif a != b and b != c and c != a:
            return 'scalene'
        else:
            return 'isosceles'
        