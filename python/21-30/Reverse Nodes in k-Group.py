class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <=1 or head==None :
            return head
        su = ListNode(0)
        su.next=head
        pre,p = su,head
        while True:
            counter=0
            while p!=None and counter < k:
                p=p.next
                counter+=1
            if counter!=k:
                break
            #p is the next k-group begin
            t = pre.next
            curpre =pre.next
            cur=curpre.next
            while cur!=p:
                curpre.next =cur.next
                pre.next=cur
                cur.next=t
                #update
                t = cur
                cur=curpre.next
            pre = curpre
        return su.next
