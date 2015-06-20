/**
 question :https://leetcode.com/problems/word-search/
 finish time : 35min
 error before ac: 0
 time complexity: O(row*col*len(word))
 space complexity: O(1)
*/

class Solution {
public:
    bool dfs(vector<vector<bool> >&base, vector<vector<char>>& board, string word,int ind,int x, int y){
      if(ind==word.size())
        return true;
      base[x][y]=true;
      int row = board.size();
      int col = board[0].size();
      if(x>0&&!base[x-1][y]&&board[x-1][y]==word[ind])
        if(dfs(base,board,word,ind+1,x-1,y))
          return true;
      if(x<row-1&&!base[x+1][y]&&board[x+1][y]==word[ind])
        if(dfs(base,board,word,ind+1,x+1,y))
          return true;
      if(y>0&&!base[x][y-1]&&board[x][y-1]==word[ind])
        if(dfs(base,board,word,ind+1,x,y-1))
          return true;
      if(y<col-1&&!base[x][y+1]&&board[x][y+1]==word[ind])
        if(dfs(base,board,word,ind+1,x,y+1))
          return true;
      base[x][y]=false;
      return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
      if(board.size()==0|| board[0].size()==0||word.size()==0)      
        return false;
      int row,col;
      row = board.size();
      col = board[0].size();
      if(row*col < word.size())
        return false;
      //iteration the 2d board
      vector<vector<bool> > base(row,vector<bool>(col,false));
      for(int i=0; i<row; i++){
        for(int j =0; j<col; j++){
          if(board[i][j]==word[0])
            if(dfs(base,board,word,1,i,j))
                return true;
        }
      }
      return false;
    }
};
