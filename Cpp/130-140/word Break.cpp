class Solution {
public:
  //o(n^2) time   
  // 12ms
  // 4 error   2 write fault object , 1 substr index error , 1 count!=0 forget
    bool wordBreak(string s, unordered_set<string>& wordDict) {
      int size = s.size();
      if(size == 0)
        return true;
      vector<bool> base(size+1,false);  //error 1   vector<int>
      base[0] = true;
      for(int i=0; i<s.size(); i++){ // error 4 wordDict.size()
        for(int j=0; j<i+1; j++)
          if(base[j]&&wordDict.count(s.substr(j,i+1-j))!=0){   //error 2,3  wordDict.count(s.substr(j,i+1));
            base[i+1] = true;
            break;
          }
      }
      return base[size];
    }
};
