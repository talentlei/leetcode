/*
 find kth largest element in binary search tree
*/
typedef struct TreeNode{
  int val;
  TreeNode * left;
  TreeNode * right;
  TreeNode(int x): val(x),left(NULL),right(NULL){};
};
class Solution{
  int getNum(TreeNode * root){
    if(root==NULL)
      return 0;
    return getNum(root->left)+getNum(root->right)+1;
  }
  int getKthLargest(TreeNode * root,int k){
    int num = getNum(root);
    if(num<k)
      return -1;
    int lk = num-k+1;
    int cnt=0;
    stack<TreeNode*> myStack;
    TreeNode* temp = root;
    while(!myStack.empty()||temp!=NULL){
        while(temp!=NULL){
         myStack.push(temp);
          temp = temp->left;
        }
        temp = myStack.top();
        myStack.pop();
        cnt++;
        if(cnt==lk)
          return temp->val;
        temp = temp->right;
    }
    return temp->val;
  }
};


/*
 find kth largest element in binary search tree
 recursion method. it contain repeat computing. 
 to improve this， you can store some userful infor.
 
*/
typedef struct TreeNode{
  int val;
  TreeNode * left;
  TreeNode * right;
  int lcnt;
  int rcnt;
  TreeNode(int x): val(x),left(NULL),right(NULL){},lcnt(0),rcnt(0);
};
class Solution{
  int solve(TreeNode * root,int k){
   getNum(root);
   return getKthLargest(root,k);
  }
  void getNum(TreeNode * root){
    if(root==NULL)
      return 0;
    root->lcnt = getNum(root->left);
    root->rcnt = getNum(root->right);
  }
  int getKthLargest(TreeNode * root,int k){
    if(root->rcnt == k-1)
     return root->val;
    if(root->rcnt >k-1)
     return getKthLargest(root->right, k);
    else return getKthLargest(root->left,k-root->rcnt-1);
  }
};
