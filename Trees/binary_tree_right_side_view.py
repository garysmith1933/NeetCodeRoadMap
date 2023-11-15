class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            right = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right) 
            if right:
                res.append(right.val)
        return res
            # Time O(N) #Space O(N)
      