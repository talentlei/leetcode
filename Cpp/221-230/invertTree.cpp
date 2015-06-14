    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL)
            return root;
        TreeNode* tl = invertTree(root->left);
        TreeNode* tr = invertTree(root->right);
        root->left = tr;
        root->right = tl;
        return root;
        
    }
