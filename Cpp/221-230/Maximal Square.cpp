class Solution {
public:
#include <cmath>
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
      int edge = 0;
      if(matrix.size()==0|| matrix[0].size()==0)
        return edge*edge;
      int row = matrix.size();
      int col = matrix[0].size();
      vector<vector<int> > base(2,vector<int>(col,0));
      int res=0;
      for(int j=0; j<col; j++)
        if(matrix[0][j]=='1'){
            base[0][j] = 1;
            res = 1;
        }
      for(int i=1; i<row; i++){
        if(matrix[i][0] == '1')
          base[i%2][0] = 1;
        else base[i%2][0] = 0;
        for(int j=1; j<col; j++)
            if(matrix[i][j]=='1')
                base[i%2][j] = min(min(base[(i-1)%2][j-1],base[(i-1)%2][j]),base[i%2][j-1])+1;
            else base[i%2][j]=0;
        int tmp = *max_element(base[i%2].begin(),base[i%2].end());
        if(tmp > res)
            res = tmp;
      }
      return res*res;
    }
};
};
