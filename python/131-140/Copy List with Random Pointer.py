    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return None
        origin,rori = {},{}
        new={}
        count=0
        p=head
        while p!=None:
            temp=RandomListNode(p.label)
            origin[count]=p
            rori[p]=count
            new[count]=temp
            count+=1
            p=p.next
        for i in range(count):
            if i ==count-1:
                new[count-1].next=None
            else:
                new[i].next=new[i+1]
            if origin[i].random==None:
                new[i].random=None
            else:
                new[i].random=new[rori[origin[i].random]]
        return new[0]
