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
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None or (root.left==None and root.right==None):
            return True
        result = self.inorderTraversal(root)
        for i in range(1,len(result)):
            if result[i]<=result[i-1]:
                return False
        return True
