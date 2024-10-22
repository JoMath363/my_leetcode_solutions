class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = set(s)
        a = []

        for i in s:
            if i.isnumeric() :
                a.append(int(i))

        a.sort()

        if len(a) < 2:
            return -1
        return a[-2]

        