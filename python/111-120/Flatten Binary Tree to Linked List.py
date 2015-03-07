    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        record=[]
        result=[]
        p = root
        while p!=None or len(record)!=0:
            while p!=None:
                record.append(p)
                result.append(p)
                p=p.left
            p = record.pop()
            p=p.right
        for i in range(0,len(result)-1):
            result[i].right=result[i+1]
            result[i].left=None
