    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        temphead = ListNode(0)
        temphead.next=head
        pre,cur = temphead,head.next
        while cur!=None:
            if pre.next.val == cur.val:
                while cur!=None and cur.val==pre.next.val:
                    cur = cur.next
                pre.next=cur
                if cur !=None:
                    cur=cur.next
            else:
                pre =pre.next
                cur = cur.next
        return temphead.next
