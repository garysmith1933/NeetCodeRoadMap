class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = set()

        stack = [ root ]

        while stack:
            node = stack.pop()
        
            visited.add(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
    
        return sorted(visited)[k-1]
    
    #Time O(N * Log(N))