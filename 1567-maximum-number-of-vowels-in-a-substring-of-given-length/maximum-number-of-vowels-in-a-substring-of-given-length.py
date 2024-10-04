class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        total = 0
        for c in s[:k]:
            if c in vowels:
                total += 1

        maxVowel = total

        for i in range(len(s)-k):
            if s[i] in vowels:
                total -= 1
            if s[i+k] in vowels:
                total += 1

            maxVowel = max(maxVowel, total)

        return maxVowel