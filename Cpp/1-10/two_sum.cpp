
/**
    runtime : 20ms
    error: 2   ind1!=ind2    
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
              if(i+1==iter->second)  continue;
              res[0] = min(i+1,iter->second);
              res[1] = max(i+1,iter->second);
              break;
          }
        }return res;
    }
};
