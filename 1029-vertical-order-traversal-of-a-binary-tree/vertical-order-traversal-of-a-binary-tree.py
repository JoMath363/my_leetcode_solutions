# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
    
        def bfs(node, x, y):
            if node:
                mp[x].append((y, node.val))    
                bfs(node.left, x - 1, y + 1)
                bfs(node.right,  x + 1, y + 1)

        bfs(root, 0, 0)

        res = []
        for key in sorted(mp.keys()):
            res.append([val for _, val in sorted(mp[key])])

        return res



            