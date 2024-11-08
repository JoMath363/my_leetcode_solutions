class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 1

        for i in range(len(colors)): 
            for j in range(1, len(colors)):
                if colors[i] != colors[j]:
                    res = max(j - i, res)

        return res
