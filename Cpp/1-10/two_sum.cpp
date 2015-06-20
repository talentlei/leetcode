
/**
    
*/
class Solution1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> myMap;
        vector<int> res(2,0);
        for(int i=0; i<nums.size();i++)
          myMap[nums[i]]=i+1;
        unordered_map<int,int>::iterator iter;
        for(int i=0; i<nums.size(); i++){
          iter = myMap.find(target-nums[i]);
          if(iter!=myMap.end()){
            if(nums[i]>iter->first){
              res[0] = i+1;
              res[1] = iter->second;
              }
              else{
                res[0]=iter->second;
                res[1] = i+1;
              }
              break;
          }
        }return res;
    }
};
