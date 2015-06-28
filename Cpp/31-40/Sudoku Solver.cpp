/*
    runtime: 40ms
    error: 0

*/
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        dfs(board,0,0);
    }
    bool dfs(vector<vector<char> >& board , int row, int col){
        for(int i=row; i< 9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j]=='.'){
                    for(int k =1; k<=9; k++){
                        if(isvalid(board,i,j,k)){
                            board[i][j] = '0'+k;
                            if(dfs(board,i,j)) return true;
                        }
                    }
                    board[i][j]='.';
                    return false;
                }
            }
        }
        return true;
    }
    bool isvalid(vector<vector<char> > & board, int row, int col, int val){
          char ch = '0'+val;
          for(int j=0; j<9; j++){
              if(board[row][j]==ch)
                return false;
          }
        //check row
        for(int i=0; i<9; i++){
            if(board[i][col]==ch)
              return false;
          }
        //check square
            int prow = row/3;
            int pcol = col/3;
            for(int i = prow*3; i<prow*3+3; i++){
              for(int j = pcol*3; j <pcol*3+3; j++){
                if(board[i][j]==ch)
                  return false;
              }
            }
          return true;
    }
};
    
