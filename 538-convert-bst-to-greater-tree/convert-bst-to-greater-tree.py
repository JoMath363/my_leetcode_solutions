# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        cur = root
        acc = 0

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right

            cur = stack.pop()
            acc += cur.val
            cur.val = acc

            cur = cur.left

        return root
