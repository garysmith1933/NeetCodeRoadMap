class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            
            # if the node is greater than the max value its greater than every other node that came before it, 
            #so we can count it 
            res = 1 if node.val >= maxVal else 0
            # we update the max value so we only need to compare it to the next node in the path instead of keeping
            # record of all the nodes in the path.
            maxVal = max(node.val, maxVal)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)

        #Time O(N) Space O(N)