class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # empty root
            return False
    
        def dfs(root, total):
            if not root:
                return total == targetSum
            
            total += root.val

            return dfs(root.left, total) or dfs(root.right, total)
        
        return dfs(root, 0)
        