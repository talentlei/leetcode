    def reverseBetween(self, head, m, n):
        if head==None or m==n:
            return head
        thead=ListNode(0)
        thead.next=head
        pre,cur=thead,head
        i=0
        while i<m-1:
            cur=cur.next
            pre=pre.next
            i+=1
        tpre=pre
        t=cur
        cur=cur.next
        pre=pre.next
        i=0
        while i <n-m:
            tpre.next=cur
            pre.next=cur.next
            cur.next=t
            t=cur
            cur=pre.next
            i+=1
        return thead.next
