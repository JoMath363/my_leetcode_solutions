# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        count = 0

        while stack:
            cur = stack.pop()

            if not cur:
                continue

            stack.append(cur.left)
            stack.append(cur.right)

            count += 1

        return count