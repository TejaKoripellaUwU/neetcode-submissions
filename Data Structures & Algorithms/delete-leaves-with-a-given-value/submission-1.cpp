/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int targ{};
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        targ = target;
        if (dfs(root)){
            delete root;
            return nullptr;
        }
        return root;
    }

    bool dfs(TreeNode* cur){

        if (cur->left == nullptr && cur->right == nullptr && cur->val == targ){
            return true;
        }
        int nt = 0;
        if (!cur->left || dfs(cur->left)){
            nt++;
            delete cur->left;
            cur->left = nullptr;
        }
        if (!cur->right || dfs(cur->right)){
            nt++;
            delete cur->right;
            cur->right = nullptr;
        } 
        if (nt == 2 && cur->val == targ){
            return true;
        }
        return false;
    }
};