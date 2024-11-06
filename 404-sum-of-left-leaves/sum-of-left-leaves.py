# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        res = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if cur.left and not cur.left.left and not cur.left.right:
                res += cur.left.val

            cur = cur.right

        return res
