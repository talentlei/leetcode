/*
 find kth largest element in binary search tree
*/
struct {
  int val;
  TreeNode * left;
  TreeNode * right;
}TreeNode;
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
    myStack.push(root);
    TreeNode* temp = root;
    while(！myStack.empty()){
        while(temp!=NULL){
          temp = temp->left;
          myStack.push(temp);
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
