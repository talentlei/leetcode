class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        pro = 1
        product = [0 for i in xrange(n)]
        for i in xrange(1,n+1):
            pro = pro*i
            product[i-1]=pro
        
        res = [i+1 for i in xrange(n)]
        k=k-1
        i=n-2
        while i>=0 and k>0:
            pb = k/product[i]
            tmp = res[n-2-i:]
            tmp.sort()
            t = tmp[pb]
            pos = n-2-i
            while pos <n and res[pos]!= t:
                pos+=1
            res[pos],res[n-2-i] = res[n-2-i],res[pos]
            tmp = res[n-2-i+1:]
            tmp.sort()
            res = res[:n-2-i+1]+tmp
            k = k-product[i]*pb
            i-=1
        tres = [str(i) for i in res]
        return ''.join(tres)
        
        
