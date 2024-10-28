# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def bsf(node, depth):
            if not node: return

            if depth >= len(ans):
                ans.append([node.val])
            else:
                ans[depth].append(node.val)

            bsf(node.left, depth + 1)
            bsf(node.right, depth + 1)

        bsf(root, 0)
        
        return ans
            


        