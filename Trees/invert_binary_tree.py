class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([ root ])
        while queue:
            node = queue.popleft()

            temp = node.right
            node.right = node.left
            node.left = temp

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return root
    # Time O(N) Space O(N)