"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root

        if not root.children:
            return [root.val]

        nodes = []
        for node in root.children:
            nodes += self.postorder(node)

        return nodes + [root.val]