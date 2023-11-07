class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #need to implement logic to get the max count of edges on each side, and add the edges of each side to get the answer
        # recurision 
        # helper function to recursively handle count of each side

        left = self.depth(root.left , 1)
        right = self.depth(root.right, 1)

        print(left, right)

        return left + right
    
    def depth(self, root: Optional[TreeNode], count: int ) -> int:
        # None value
        if root == None: 
            return count - 1
        
        left = self.depth(root.left, count + 1)
        right = self.depth(root.right, count + 1)
        
        count = max(left, right)
        
        return count

