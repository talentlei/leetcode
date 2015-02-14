# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next ==None:
            return head
        su = ListNode(0)
        su.next = head
        p = head
        pre,slow,fast =su,p,p.next
        while fast!=None:
            pre.next = fast
            slow.next=fast.next
            fast.next = slow
            #update
            pre=slow
            if slow.next == None or slow.next.next==None:
                break
            else:
                fast =pre.next.next
                slow = pre.next
        return su.next
