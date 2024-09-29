class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        i = 0

        for j, char in enumerate(typed):
            if i < len(name) and name[i] == char:
                i += 1
            elif j == 0 or char != typed[j - 1]:
                return False

        return i == len(name)


        