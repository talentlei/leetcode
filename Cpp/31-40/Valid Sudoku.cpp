class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //check row , col ,square;
        unordered_set<int> rowSet,colSet;
        for(int i=0; i<9; i++){
          for(int j=0; j<9; j++){
            if(board[i][j]=='.')  continue;
            if(colSet.find(board[i][j])!=colSet.end())
              return false;
            colSet.insert(board[i][j]);
          }
          colSet.clear();
        }
        //check row
        for(int i=0; i<9; i++){
          for(int j=0; j<9; j++){
            if(board[j][i]=='.')  continue;
            if(rowSet.find(board[j][i])!=rowSet.end())
              return false;
            rowSet.insert(board[j][i]);
          }
          rowSet.clear();
        }
        //check square
        for(int i=0; i<3; i++)
          for(int j=0; j<3; j++){
            for(int row = i*3; row<i*3+3; row++)
              for(int col = j*3; col <j*3+3; col++){
                if(board[row][col]=='.')  continue;
                if(colSet.find(board[row][col])!=colSet.end())
                  return false;
                colSet.insert(board[row][col]);
              }
          colSet.clear();  
          }
          return true;
    }
};
