class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0 , num

        while l <= r:
            mid = (l + r) // 2
            n = mid ** 2

            if n == num:
                return True
            elif n > num:
                r = mid - 1
            elif n < num: 
                l = mid + 1

        return False