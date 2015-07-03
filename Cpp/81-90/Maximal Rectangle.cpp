/*
    runtime:28ms
    error: 0

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
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size()==0||matrix[0].size()==0) return 0;
        int row = matrix.size();
        int col = matrix[0].size();
        for(int i=0; i<row; i++)
            matrix[i].push_back(0);
        int Max=0; vector<int> height(col+1,0);
        for(int i=0; i<row; i++){
            for(int j=0; j<col+1; j++)
                height[j] = (matrix[i][j]=='1')?height[j]+1:0;
            int Area = largestRectangleArea(height);
            Max = max(Max,Area);
        }
     return Max;   
    }
};
