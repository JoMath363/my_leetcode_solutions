class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = word[0] == word[0].upper() and word[1:] == word[1:].lower()

        if word == word.upper() or word == word.lower() or capital:
            return True
        return False