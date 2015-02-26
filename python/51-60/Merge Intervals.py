 # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals or len(intervals)<=1:
            return intervals
        B=sorted(intervals,key=lambda x:(x.start,x.end))
        result = []
        cur = Interval(B[0].start,B[0].end)
        i = 1
        while i <len(B):
            if cur.end <B[i].start:
                result.append(cur)
                cur=B[i]
            elif cur.end <B[i].end:
                cur.end=B[i].end
            i+=1
        result.append(cur)
        return result
