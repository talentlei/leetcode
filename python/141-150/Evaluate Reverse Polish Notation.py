    def evalRPN(self, tokens):
        stack=[]
        operator = ['+','-','*','/']
        for i in tokens:
            if i in operator:
                op2 = stack.pop()
                op1 = stack.pop()
                if i=='+':
                    stack.append(op1+op2)
                elif i=='-':
                    stack.append(op1-op2)
                elif i=='*':
                    stack.append(op1*op2)
                elif i=='/':
                    stack.append(op1/op2)  #have some error in /
            else:
                stack.append(int(i))
        return stack[0]
