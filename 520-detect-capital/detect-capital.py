class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = word == word.upper() 
        lower = word == word.lower()
        capital = word[0] == word[0].upper() and word[1:] == word[1:].lower()

        if upper or lower or capital:
            return True
        return False