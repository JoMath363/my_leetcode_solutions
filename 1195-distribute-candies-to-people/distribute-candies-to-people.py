class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        P = [0] * num_people
        c = candies
        i, n = 0, 0

        while c > 0:
            if c - (n + 1) > 0:
                n += 1
                P[i] += n
                c -= n
            else:
                P[i] += c
                c = 0

            i += 1
            if not i < len(P):
                i = 0

        return P
            