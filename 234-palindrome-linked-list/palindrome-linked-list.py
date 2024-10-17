# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1

        while i < j:
            if nodes[i].val != nodes[j].val:
                return False
            i += 1
            j -= 1
        return True