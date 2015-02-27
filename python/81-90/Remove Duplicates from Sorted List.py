    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
        pre,cur = head,head.next
        while cur!=None:
            if pre.val == cur.val:
                pre.next=cur.next
                cur=cur.next
            else:
                pre =cur
                cur = cur.next
        return head
