class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        n = len(mat)
        ans = 0

        for i in range(n):
            ans += mat[n - i - 1][i]
            ans += mat[i][i]

        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]

        return ans


