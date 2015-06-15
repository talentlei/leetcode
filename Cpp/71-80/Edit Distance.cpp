class Solution {
public:
    //DP mehtod 
    int minDistance(string word1, string word2) {
        if(word1==word2)
          return 0;
        int size1 = word1.size();
        int size2 = word2.size();
        if(size1==0)
            return size2;
        if(size2==0)
            return size1;
        vector<vector<int> > base(size1+1,vector<int>(size2+1,0));
        for(int i=0; i<size2+1; i++)
          base[0][i] = i;
        for(int i=0; i<size1+1; i++)
          base[i][0] = i;
        for(int i=1; i<=size1; i++){
          for(int j=1; j<=size2; j++){
            if(word1[i-1]==word2[j-1])
              base[i][j] = base[i-1][j-1];
            else base[i][j] = min(min(base[i-1][j-1],base[i-1][j]),base[i][j-1])+1;
          } 
        }
        return base[size1][size2];
    }
};
