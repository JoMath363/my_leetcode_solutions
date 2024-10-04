class Solution:
    def maxScore(self, cardsPoints: List[int], k: int) -> int:
        cards = cardsPoints[-k:] + cardsPoints[:k]
        total = sum(cards[:k])
        maxPoints = total

        for i in range(len(cards)-k):
            total -= cards[i]
            total += cards[i+k]
            maxPoints = max(maxPoints, total)

        return maxPoints