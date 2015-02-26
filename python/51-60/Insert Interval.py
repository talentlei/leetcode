    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        result=[]
        for i in range(0,len(intervals)):
            if intervals[i].end < newInterval.start or intervals[i].start > newInterval.end:
                result.append(intervals[i])
            elif newInterval.start>=intervals[i].start and newInterval.end<=intervals[i].end:
                return intervals
            elif newInterval.start<=intervals[i].start and newInterval.end>=intervals[i].end:
                continue
            elif newInterval.start>=intervals[i].start:
                newInterval.start=intervals[i].start
            elif newInterval.end <= intervals[i].end:
                newInterval.end = intervals[i].end
        result.append(newInterval)
        result.sort(cmp=None, key=lambda x:x.start, reverse=False)
        return result
