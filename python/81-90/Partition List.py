   # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head==None or head.next==None:
            return head
        thead = ListNode(0)
        thead.next=head
        pre,cur=thead,head
        while cur!=None and cur.val<x:
            cur = cur.next
            pre = pre.next
        if cur==None:
            return head
        pt,t = pre,cur
        cur=cur.next
        pre=pre.next
        while cur!=None:
            if cur.val<x:
                pt.next=cur
                pt=pt.next
                pre.next=cur.next
                cur.next=t
                cur=pre.next
            else:
                cur = cur.next
                pre = pre.next
        return thead.next
