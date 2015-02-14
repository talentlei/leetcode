# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        su = ListNode(0)
        head = su
        while l1!=None and l2!=None:
            if l1.val <l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 =l2.next
            head = head.next
            head.next=None
        if l1!=None:
            head.next = l1
        else:
            head.next = l2
        return su.next
