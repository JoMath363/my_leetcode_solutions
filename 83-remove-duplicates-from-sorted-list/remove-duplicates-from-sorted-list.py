# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        prev = None

        while cur:
            if cur.val in stack:
                prev.next = cur.next
            else:
                stack.append(cur.val)
                prev = cur
            
            cur = cur.next

        return head




        