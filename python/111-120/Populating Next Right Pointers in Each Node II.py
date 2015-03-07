if root ==None:
            return
        upper,down=[],[]
        upper.append(root)
        while len(upper)!=0:
            i=0
            pre = TreeLinkNode(0)
            while i<len(upper):
                node=upper[i]
                pre.next=node
                pre = node
                if node.left!=None:
                    down.append(node.left)
                if node.right!=None:
                    down.append(node.right)
                i+=1
            upper=[]
            if len(down)>0:
                upper=down[:]
                down=[]
