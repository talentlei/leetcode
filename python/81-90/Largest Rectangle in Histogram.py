    # @param {integer[]} height
    # @return {integer}
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
