class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first, second = 0, None
        res = 0
        for i in range(1, len(colors)):
            if colors[i] != colors[first]:
                if not second:
                    second = i
                res = max(res, i - first)   
            else:
                if second:
                    res = max(res, i - second)
        
        return res
