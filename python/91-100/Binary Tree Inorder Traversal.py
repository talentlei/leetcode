    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack=[]
        result=[]
        p=root
        while p!=None or len(stack)>0:
            while p!=None:
                stack.append(p)
                p=p.left
            p=stack.pop()
            result.append(p.val)
            p=p.right
        return result
