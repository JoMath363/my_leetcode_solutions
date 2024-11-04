class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for i in sorted(asteroids):
            if i > mass:
                return False
            mass += i
        return True