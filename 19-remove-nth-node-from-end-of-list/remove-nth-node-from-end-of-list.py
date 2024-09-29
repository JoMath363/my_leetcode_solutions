# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        nodes = []
        current = head
        length = 0

        while current:
            nodes.append(current)
            current = current.next
            length += 1

        index = length - n
        if length == 1:
            head = None
        elif nodes[index] == head:
            head = head.next
        elif nodes[index].next:
            nodes[index - 1].next = nodes[index + 1]
        else:
            nodes[index - 1].next = None

        return head

        

        