# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
            if not root:
                return ''

            l = f'({self.tree2str(root.left)})'
            r = f'({self.tree2str(root.right)})'

            if root.right:
                return f'{root.val}{l}{r}'

            if root.left:
                return f'{root.val}{l}'
            
            return f'{root.val}'

            
            
        