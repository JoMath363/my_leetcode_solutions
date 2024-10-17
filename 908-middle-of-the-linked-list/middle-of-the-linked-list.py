# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length, cur = 0, head

        while cur:
            length += 1
            cur = cur.next

        index, target = 0, head

        while index < length // 2:
            index += 1
            target = target.next

        return target

