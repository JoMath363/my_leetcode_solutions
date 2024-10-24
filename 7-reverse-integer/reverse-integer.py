class Solution:
    def reverse(self, x: int) -> int:
        
        ans = str(x)[::-1]

        if x < 0:
            ans = -int(ans[:-1])
        else:
            ans = int(ans)

        if ans < (-2 ** 31) or ans > (2 ** 31 + 1):
            return 0
        return ans
        
