# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dsf(node, arr):
            if not node:
                return

            if not (node.left or node.right):
                arr.append(node.val)

            dsf(node.left, arr)
            dsf(node.right, arr)

            return arr

        return dsf(root1, []) == dsf(root2, [])