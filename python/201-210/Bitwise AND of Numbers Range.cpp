class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if (m==n)
            return m;
        unsigned int flag = 1;
        unsigned int t;
        int res=0;
        for(int i=31; i>=0; i--){
            t = flag<<i;
            if(((m&t)!=(n&t)))
                break;
            res |= (n&t);
        }
        return res;
    }
};
