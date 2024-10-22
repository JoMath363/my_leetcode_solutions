class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        c = ''
        b = bin(n)

        for i in range(2, len(b)):
            c += '0' if b[i] == '1' else '1'

        return int(c, 2)
                
        


        