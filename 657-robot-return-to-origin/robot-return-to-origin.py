class Solution:
    def judgeCircle(self, moves: str) -> bool:
        res = [0, 0]

        for m in moves:
            if m == 'U':
                res[0] += 1
            elif m == 'D':
                res[0] -= 1
            elif m == 'R':
                res[1] += 1
            else:
                res[1] -= 1

        return res == [0, 0]
