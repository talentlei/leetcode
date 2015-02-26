 # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        m,n = len(a),len(b)
        if m == 0:
            return b
        if n==0:
            return a
        a=a[::-1]
        b=b[::-1]
        pos,re = 0,0
        result = []
        while pos <m and pos < n:
            temp = int(a[pos])+int(b[pos])+re
            re = temp//2
            result.append(temp%2)
            pos +=1
        c = []
        if pos != m:
            c = a[pos:]
        if pos != n:
            c = b[pos:]
        if len(c)>0:
            if re ==0:
                result.extend(c)
            else :
                for i in range(0,len(c)):
                    temp = int(c[i])+re
                    re = temp//2
                    result.append(temp%2)
        if re ==1 :
            result.append(1)
        result.reverse()
        result = [str(a) for a in result]
        s=''.join(result)
        return s
