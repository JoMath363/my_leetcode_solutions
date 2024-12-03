class Solution:
    def isBalanced(self, num: str) -> bool:
        odd, even = 0, 0

        for i, n in enumerate(num):
            if i % 2 == 0:
                even += int(n)
            else:
                odd += int(n)

        return odd == even