class Solution {
public:
    //method 1  o(kn)time o(1)space   naive
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int len = nums.size();
        for(int i=0; i<len; i++){
          for(int j=i+1; j<=i+k&& j<len; j++)
            if(nums[i]==nums[j])
              return true;
        }
        return false;
    }
    //method 2 o(n)time  o(n)space
    bool containsNearbyDuplicate2(vector<int>& nums, int k) {
        map<int,int> record;
        int len=nums.size();
        for(int i=0; i<len; i++){
          if(record.count(nums[i])==0)
            record[nums[i]]=i;
          else{
            if(i-record[nums[i]]<=k)
              return true;
            record[nums[i]] = i;
          }
        }
        return false;
    }
};
