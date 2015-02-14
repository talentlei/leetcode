# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        su = ListNode(0)
        su.next=head
        pre,cur,p = su,head,head
        for i in range(0,n):
            p=p.next
        while p!=None:
            p=p.next
            cur=cur.next
            pre=pre.next
        pre.next=cur.next
        return su.next
