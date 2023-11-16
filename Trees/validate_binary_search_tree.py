class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            
            if not ( left < node.val < right ):
                return False
            
            # every node on the left side should be less than the previous node
            # every node on the right side should be greater than the previous node
            return (valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))

        
        return valid(root, float("-inf"), float("inf"))

        #Time O(N) Space O(N)