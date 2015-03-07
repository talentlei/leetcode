    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root ==None:
            return []
        result=[]
        upper,down=[],[]
        upper.append(root)
        toLeft=True
        while len(upper)!=0:
            temp=[]
            i=len(upper)-1
            while i>=0:
                node=upper[i]
                temp.append(node.val)
                if toLeft:
                    if node.left!=None:
                        down.append(node.left)
                    if node.right!=None:
                        down.append(node.right)
                else:
                    if node.right!=None:
                        down.append(node.right)
                    if node.left!=None:
                        down.append(node.left)
                i-=1
            toLeft=not toLeft
            result+=[temp]
            upper=[]
            if len(down)>0:
                upper=down[:]
                down=[]
        return result
