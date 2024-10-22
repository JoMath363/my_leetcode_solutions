class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        res = []

        for [x, y, r] in queries:
            count = 0

            for p in points:
                h = sqrt((x - p[0]) ** 2 + (y - p[1]) ** 2)
                if h <= r:
                    count += 1
            res.append(count)

        return res

                
        