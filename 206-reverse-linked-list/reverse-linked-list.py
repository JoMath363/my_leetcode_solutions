# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        head.next = None
        for i in range(1, len(nodes)):
            nodes[i].next = nodes[i-1]

        return nodes[-1]
