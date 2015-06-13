class Solution {
public:
    void dfs(vector<int > &one,int deep,int k, int n,int start){
      if(deep == k){
            if(n==0)
                res.push_back(one);
            return ;
      }
      for(int i=start; i<9; i++){
        one[deep]=i+1;
        dfs(one,deep+1,k,n-i-1,i+1);
      }
      return;
    }
    vector<vector<int> > combinationSum3(int k, int n) {
          if(k>9||k<=0||k>n||n>9*k)
            return res;
          vector<int> one(k,0);
          dfs(one,0,k,n,0);
          return res;
    }
private:
    vector<vector<int> > res;
};
