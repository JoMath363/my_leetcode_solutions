# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        cur = head
        prev = None

        while cur:
            if cur.val == val:
                if cur == head:
                    head = head.next
                elif not cur.next:
                    prev.next = None
                else:
                    prev.next = cur.next
                    cur = cur.next 
                    continue

            prev = cur
            cur = cur.next

        return head