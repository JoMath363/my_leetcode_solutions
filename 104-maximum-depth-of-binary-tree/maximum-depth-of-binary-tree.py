# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def getHeight(node, count = 0):
            if node == None:
                return count

            left = getHeight(node.left, count + 1)
            right = getHeight(node.right, count + 1)

            return max(left, right)

        return getHeight(root)

        