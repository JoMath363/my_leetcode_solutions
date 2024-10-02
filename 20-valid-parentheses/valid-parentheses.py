class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack

        