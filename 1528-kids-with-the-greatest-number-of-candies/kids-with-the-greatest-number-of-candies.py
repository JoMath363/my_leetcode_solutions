class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        ans = [c + extraCandies >= maxCandy for c in candies]

        return ans
