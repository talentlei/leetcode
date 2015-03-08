    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root==None:
            return []
        result=[]
        stack=[root]
        pre = None
        while len(stack)>0:
            cur=stack[len(stack)-1]
            if (cur.left==None and cur.right==None) or (pre!=None and(cur.left==pre or cur.right==pre)):
                result.append(cur.val)
                stack.pop()
                pre=cur
            else:
                if cur.right!=None:
                    stack.append(cur.right)
                if cur.left!=None:
                    stack.append(cur.left)
        return result
