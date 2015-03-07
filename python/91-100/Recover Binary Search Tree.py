    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        stack=[]
        nodes=[]
        prenode=None
        p=root
        while p!=None or len(stack)>0:
            while p!=None:
                stack.append(p)
                p=p.left
            p=stack.pop()
            if len(nodes)==0 and prenode!=None:
                if prenode.val > p.val:
                    nodes.append(prenode)
                    nodes.append(p)
            elif len(nodes)>0:
                if prenode.val > p.val:
                    nodes[1]=p
            prenode = p
            p=p.right
        tval = nodes[0].val
        nodes[0].val = nodes[1].val
        nodes[1].val = tval
        return root
