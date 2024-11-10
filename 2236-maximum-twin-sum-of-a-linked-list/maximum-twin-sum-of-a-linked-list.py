# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        stack = []
        cur = head

        while cur:
            stack.append(cur)
            cur = cur.next

        i, j = 0, len(stack) - 1
    
        while i < j:
            n = stack[i].val + stack[j].val
            res = max(res, n)
            i += 1
            j -= 1

        return res

