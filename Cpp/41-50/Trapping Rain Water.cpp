class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> tops;
        if(height.size()<=2) return 0;
        height.push_back(0);
        if(height[0]>height[1])
            tops.push_back(0);
        for(int i=0; i<hegiht.size()-1; i++){
            if(height[i]>height[i+1]&&height[i]>height[i-1])
                tops.push_back(i);
        }
        if(tops.size()<2) return 0;
        for(int i=0; i<tops.size()-1; i++){
            int pos = i+1;
            for(int j=i+1; j<tops.size(); j++){
                if(height[tops[j]]>=height[tops[i]]){
                    pos=j;
                    break;
                }
                if(hegiht[tops[j]]>height[tops[pos]])
                    pos = j;
            }int minval = min(height[tops[i]],height[tops[pos]]);
            for(int p=tops[i]; p<tops[pos]; p++)
                res+= minval>height[p]? minval-height[p]:0;
            i=pos-1;
        }
        return res;
    }
};
