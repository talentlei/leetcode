/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  // method 1  travel the tree o(n)time;
    int countNodes(TreeNode* root) {
        
        if(root==NULL)
            return 0;
        int right=0,left=0;
        if(root->left!=NULL)
            left = countNodes(root->left);
        if(root->right!=NULL)
            right = countNodes(root->right);
        return left+right+1;
    }
    //method 2
   int countNodes(TreeNode* root) {
        if(!root) return 0;
        int hl=0, hr=0;
        TreeNode *l=root, *r=root;
        while(l) {hl++;l=l->left;}
        while(r) {hr++;r=r->right;}
        if(hl==hr) return pow(2,hl)-1;
        return 1+countNodes(root->left)+countNodes(root->right);
    }
};
