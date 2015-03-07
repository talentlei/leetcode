    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root ==None:
            return []
        result=[]
        upper,down=[],[]
        upper.append(root)
        while len(upper)!=0:
            i=0
            temp=[]
            while i<len(upper):
                node=upper[i]
                temp.append(node.val)
                if node.left!=None:
                    down.append(node.left)
                if node.right!=None:
                    down.append(node.right)
                i+=1
            result+=[temp]
            upper=[]
            if len(down)>0:
                upper=down[:]
                down=[]
        return result
