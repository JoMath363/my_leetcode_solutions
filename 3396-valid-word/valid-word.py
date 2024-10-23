class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        hm = {'v': 0, 'c': 0 }

        for char in word.lower():
            if char.isdigit():
                continue

            if char.isalpha():
                if char in 'aeiou':
                    hm['v'] += 1
                else:
                    hm['c'] += 1
                continue
            
            return False
        
        if len(word) > 2 and hm['v'] > 0 and hm['c'] > 0:
            return True
        return False


        