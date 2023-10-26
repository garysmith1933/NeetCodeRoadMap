class Solution:
    def maxDepth(self, root: Optional[TreeNode], maxDepth=0) -> int:
        if not root:
            return maxDepth

        return max(maxDepth, self.maxDepth(root.left, maxDepth + 1), self.maxDepth(root.right, maxDepth + 1))

        # Time O(N) Space O(N)