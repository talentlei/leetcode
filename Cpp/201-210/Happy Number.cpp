class Solution {
public:
    int getNext(int n){
        int sum=0;
        int tmp = n;
        while(tmp!=0){
            int re = tmp%10;
            tmp = tmp/10;
            sum+=re*re;
        }
        return sum;
        
    }
    bool isHappy(int n) {
        set<int> mySet;
        int tmp = n;
        mySet.insert(tmp);
        while(tmp!=1){
            tmp = getNext(tmp);
            if(mySet.count(tmp)!=0)
                return false;
            mySet.insert(tmp);
        }
        return true;
    }
};
