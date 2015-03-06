class Solution:
    def subgenTrees(self,n,begin):
        result=[]
        if n==0:
            return [None]
        elif n==1:
            temp = TreeNode(begin)
            return [temp]
        for i in range(0,n):
            left = self.subgenTrees(i,begin)
            right = self.subgenTrees(n-i-1,begin+i+1)
            for l in range(0,len(left)):
                for r in range(0,len(right)):
                    temp = TreeNode(begin+i)
                    temp.left = left[l]
                    temp.right = right[r]
                    result.append(temp)
        return result
    # @return a list of tree node
    def generateTrees(self, n):
        result = self.subgenTrees(n,1)
        return result
