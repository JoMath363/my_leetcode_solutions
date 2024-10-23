class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        v, c = 0, 0

        for char in word.lower():
            if char.isdigit():
                continue

            if char.isalpha():
                if char in 'aeiou':
                    v += 1
                else:
                    c += 1
                continue
            
            return False
        
        if len(word) > 2 and v > 0 and c > 0:
            return True
        return False


        