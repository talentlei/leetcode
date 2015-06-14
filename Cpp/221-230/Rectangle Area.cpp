class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
      int len_overlap = max(min(C,G)-max(A,E),0);
      int wid_overlap = max(min(D,H)-max(B,F),0);
      return (C-A)*(D-B)+(G-E)*(H-F)-len_overlap*wid_overlap;
    }
};
