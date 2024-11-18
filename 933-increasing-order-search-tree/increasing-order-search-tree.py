# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        in_order = root

        head = TreeNode()
        cur = head

        while stack or in_order:
            while in_order:
                stack.append(in_order)
                in_order = in_order.left

            in_order = stack.pop()
            cur.right = TreeNode(in_order.val)
            cur = cur.right

            in_order = in_order.right

        return head.right
