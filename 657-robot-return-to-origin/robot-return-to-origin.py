class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        if c['L'] == c['R'] and c['U'] == c['D']:
            return True
        return False
