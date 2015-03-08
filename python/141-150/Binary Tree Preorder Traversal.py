    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result=[]
        p=root
        stack=[]
        while p!=None or len(stack)>0:
            while p!=None:
                result.append(p.val)
                stack.append(p)
                p=p.left
            p=stack.pop()
            p=p.right
        return result
