class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
            return 0 if res < -2 ** 31 else res
        else:
            res = int(str(x)[::-1])
            return 0 if res > 2 ** 31 - 1 else res
        
        
        
