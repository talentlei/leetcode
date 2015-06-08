class Solution:
    def getNext(self,n):
        sum = 0
        nstr = str(n)
        for i in nstr:
            sum+=int(i)**2
        return sum
    # @param {integer} n
    # @return {boolean}
    record = []
    def isHappy(self, n):
        tmp = n
        self.record.append(tmp)
        while(tmp!=1):
             tmp = self.getNext(tmp)
             if tmp in self.record:
                 break
             self.record.append(tmp)
        return tmp==1

##C++ solution
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
