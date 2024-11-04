class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        curMass = mass

        for i in sorted(asteroids):
            if i > curMass:
                return False
            curMass += i

        return True