    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
        pa,pb=headA,headB
        sa,sb=1,1
        while pa.next!=None:
            sa+=1
            pa=pa.next
        while pb.next!=None:
            sb+=1
            pb=pb.next
        if pa!=pb:
            return None
        pa,pb=headA,headB
        if sa>sb:
            t=sa-sb
            while t>0:
                pa=pa.next
                t-=1
        else:
            t=sb-sa
            while t>0:
                pb=pb.next
                t-=1
        while pa!=pb:
            pa=pa.next
            pb=pb.next
        return pa
