class Solution:
    def compressedString(self, word: str) -> str: 
        word += '#'
        comp = ''
        count = 1

        for i in range(1, len(word)):
            if not word[i] == word[i - 1] or count == 9:
                comp += f'{count}{word[i-1]}'
                count = 1
            else:
                count += 1
            
        return comp



        