/*
    runtime:24ms
    error: 1  
    h = myStack.top() should be h = height[myStack.top()];

*/
class Solution {
public:
    int largestRectangleArea(vector<int>& height) {
        stack<int> myStack;
        if(height.size()==0) return 0;
        height.push_back(0);
        int Max=0;
        for(int i=0; i<height.size(); i++){
            while(!myStack.empty()&&height[i]<height[myStack.top()]){
                int h=height[myStack.top()];
                myStack.pop();
                int wid = myStack.empty()?-1:myStack.top();
                int Area = (i-1-wid)*h;
                if(Area>Max) Max = Area;
            }
            myStack.push(i);
        }
        return Max;
    }
};
