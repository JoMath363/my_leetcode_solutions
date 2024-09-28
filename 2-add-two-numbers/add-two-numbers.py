# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode()
        current = result
        adder = 0

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            num = n1 + n2 + adder

            if num > 9:
                num -= 10 
                adder = 1
            else:
                adder = 0

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 

            current.val = num

            if not (l1 or l2):
                if adder == 1:
                    current.next = ListNode(1)
            else:
                current.next = ListNode()

            current = current.next

        return result


        