
/**
 * 16ms
 * error: 1  
 * 
 * 
 */ 
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int beg=0,Max=0;
        vector<int> Map(128,-1);
        for(int i=0; i<s.size(); i++){
          if(Map[s[i]]>=beg){
            Max = max(Max,i-beg);
            beg=Map[s[i]]+1;
          }
          Map[s[i]]=i;                //error 1:  add else first time
        }
        Max =max(Max,(int)s.size()-beg);
        return Max;
    }
};
