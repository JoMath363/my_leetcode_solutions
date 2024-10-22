class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        res = []

        for [x1, y1, r] in queries:
            count = 0

            for [x2, y2] in points:
                h = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if h <= r:
                    count += 1
            res.append(count)

        return res

                
        