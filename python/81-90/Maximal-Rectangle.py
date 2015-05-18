    def largestRectangleArea(self, height):
        if len(height) ==0:
            return 0
        height.append(0)
        stack = []
        mx = 0
        for i in xrange(len(height)):
            while len(stack) >0 and height[stack[-1]]>height[i]:
                h = height[stack[-1]]
                del stack[-1]
                left = -1
                if len(stack)>0:
                    left = stack[-1]
                if (h*(i-1-left)>mx):
                    mx = h*(i-1-left)
            stack.append(i)
        return mx
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if matrix == None or len(matrix)==0 or len(matrix[0])==0:
            return 0
        row,col = len(matrix),len(matrix[0])
        mx =0
        line = [0 for i in xrange(col)]
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j]=='1':
                    line[j] += 1
                else:
                    line[j]=0
            tmx = self.largestRectangleArea(line[:])
            if tmx > mx:
                mx =tmx
        return mx
