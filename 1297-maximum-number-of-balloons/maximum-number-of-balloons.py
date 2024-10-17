class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text = text.lower()
        mp = {"b": 0, "a": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        
        for char in text:
            if char in mp:
                mp[char] += 1

        return min(mp["b"], mp["a"], mp["l"]//2, mp["o"]//2, mp["n"])
                