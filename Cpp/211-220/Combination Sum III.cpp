class Solution {
public:
    
    int dfs(vector<int> &nums,vector<int> &base,vector<int > &one,int deep,int k, int n){
      if(deep == k){
        if(n==0){
            res.push_back(one);
            return 0;
          }
        else if(n>0)
          return 1;
        else return -1;
      }
      if(n<0)
        return -1;
      for(int i=0; i<nums.size(); i++){
        if(base[i] == 1)
          continue;
        base[i] = 1;
        one.push_back(i+1);
        int flag = dfs(nums,base,one,deep+1,k,n-i-1);
        base[i] = 0;
        one.pop_back();
        if(flag<0)
          break;
      }
  
    }
    vector<vector<int>> combinationSum3(int k, int n) {
          if(k>9||k<=0||k>n||n>45)
            return res;
          vector<int > nums(9);
          vector<int > base(9);
          for(int i=1; i<=9;i++){
            nums[i-1] = i;
            base[i-1] = 0;
            }
          sort(nums.begin(),nums.end());
          vector<int> one;
          dfs(nums,base,one,0,k,n);
    }
private:
    vector<vector<int> > res;
};
