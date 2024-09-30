class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        n = str(n)
        triplets = []

        for i in range(len(n), 0, -3):
            limit = max(0, i-3)
            print(i)
            print(limit)
            triplets.append(n[limit:i])
            

        return '.'.join(triplets[::-1])