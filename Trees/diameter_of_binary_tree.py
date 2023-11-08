class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(root):
            if not root: return 0
            nonlocal res

            left, right = dfs(root.left), dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left,right)
        
        dfs(root)
        return res