class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if(obstacleGrid.size()==0|| obstacleGrid[0].size()==0)
          return 0;
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int> > vec(m,vector<int>(n,0));
        for(int i=0; i<m;i++){
          if(obstacleGrid[i][0]==0)
            vec[i][0] =1;
          else break;
        }
        for(int i=0; i<n;i++){
          if(obstacleGrid[0][i]==0)
            vec[0][i] =1;
          else break;
        }
        for(int i=1; i<m; i++)
          for(int j=1; j<n; j++)
            vec[i][j]= obstacleGrid[i][j]==1?0:vec[i-1][j]+vec[i][j-1];
        return vec[m-1][n-1];
      }
};
