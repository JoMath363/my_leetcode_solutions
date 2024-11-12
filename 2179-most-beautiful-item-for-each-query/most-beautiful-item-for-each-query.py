class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty, curr = [0], 0

        for price, beauty in items:
            curr = max(curr, beauty)
            max_beauty.append(curr)
        ans = []
        for q in queries:
            i = bisect_right(items, q, key = itemgetter(0))
            ans.append(max_beauty[i])
        return ans

                

