class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                res.append(level)
        return res
    #Time O(N) Space O(N)