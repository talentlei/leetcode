/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
class Solution {
public:
void merge(vector<Interval>& intervals,vector<Interval>& res) {
        if(intervals.size()==0) return;
        Interval temp = intervals[0];
        for(int i=1; i<intervals.size(); i++){
          if(temp.end<intervals[i].start){
            res.push_back(temp);
            temp = intervals[i];
          }
          else temp.end = max(temp.end,intervals[i].end);
        }
        res.push_back(temp);
    }
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
      vector<Interval> res;
      int size = intervals.size();
      if(size == 0){ res.push_back(newInterval); return res;}
      if(newInterval.start<=intervals[0].start)
        intervals.insert(intervals.begin(),newInterval);
      else if(newInterval.start>=intervals[size-1].start)
        intervals.push_back(newInterval);
      else{
        for(vector<Interval>::iterator iter = intervals.begin(); iter!=intervals.end(); iter++){
            if((*iter).start>newInterval.start){
            intervals.insert(iter,newInterval);
             break;
            }
        }
      }
      merge(intervals,res);
      return res;
    }
};
