# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        cuurent =0
        while l1 != 0 or l2 != 0 or current != 0:
            sum = l1.val + l2.val + current
            rem = sum % 10
            l3.next = rem
            current = sum // 10
            l1 = l1.next
            l2 = l2.next
        return l3.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
#l1.next.next.next = ListNode(6)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
#l2.next.next.next = ListNode(4)
Solution()

