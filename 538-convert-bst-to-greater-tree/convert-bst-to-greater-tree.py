# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, count):
            if node:
                count = dfs(node.right, count)
                node.val += count
                count = node.val
                count = dfs(node.left, count)
            return count
        dfs(root, 0)
        return root   
