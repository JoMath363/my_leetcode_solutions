# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inOrder = []
        self.i = -1

        stk = []
        cur = root

        while cur or stk:   
            while cur:
                stk.append(cur)
                cur = cur.left

            cur = stk.pop()
            self.inOrder.append(cur.val)

            cur = cur.right

    def next(self) -> int:
        self.i += 1

        if self.i < len(self.inOrder):
            return self.inOrder[self.i]
        else:
            return self.inOrder[0]

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.inOrder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()