/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
 /*
  
  run time: 584ms;
  error: 1   cmp放在class内了
 
 */
bool cmp(const Interval& a, const Interval& b){
      return a.start<b.start;
    }
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        if(intervals.size()==0) return res;
        sort(intervals.begin(),intervals.end(),cmp);
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
};
