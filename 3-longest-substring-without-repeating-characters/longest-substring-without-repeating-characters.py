class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLen = 0

        for i in range(len(s)):
            subStr = ''

            for j in range(i, len(s)):
                if s[j] in subStr:
                    break
                else:
                    subStr += s[j]    

            if len(subStr) > maxLen:
                maxLen = len(subStr)

        return maxLen

        