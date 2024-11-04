class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        s.append(s[0])

        for i in range(len(s) - 1):
            if not s[i][-1] == s[i+1][0]:
                return False
        return True

        