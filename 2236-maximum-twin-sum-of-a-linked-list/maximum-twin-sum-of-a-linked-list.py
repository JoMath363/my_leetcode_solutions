# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        n = len(stack)
        return max(stack[i] + stack[-i-1] for i in range(n//2))
