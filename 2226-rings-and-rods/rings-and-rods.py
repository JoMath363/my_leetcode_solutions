class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        res = 0

        for i in range(0, len(rings), 2):
            rods[rings[i+1]].add(rings[i])

        for i in rods:
            if len(rods[i]) == 3:
                res += 1

        return res