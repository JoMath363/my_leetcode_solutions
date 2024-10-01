class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        
        freq = [0] * k
 
        for i in arr:
            y = i % k
            
            if freq[(k - y) % k] != 0:
                freq[(k - y) % k] -= 1
            else:
                freq[y] += 1
    
        for i in freq:
            if i != 0:
                return False
    
        return True

        