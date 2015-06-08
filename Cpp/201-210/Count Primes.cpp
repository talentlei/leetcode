class Solution {
public:
    int countPrimes(int n) {
        if(n<=2)
            return 0;
        vector<int> base(n-1,1);
        base[0] = 0;
        for(int i=1; i<n-1;i++){
            int num = i+1;
            int step = i+1;
            if(base[i]==1){
                while(step+num<n){
                    base[step+num-1]=0;
                    step +=num;
                }
            }
        }
        int cnt = count(base.begin(),base.end(),1);
        return cnt;
    }
};
