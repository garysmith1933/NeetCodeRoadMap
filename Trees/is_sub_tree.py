class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      if not subRoot: return True
      if not root: return False

      if self.treeCompare(root,subRoot): return True
      
      return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

       
    def treeCompare(self, root, subRoot):
        if not root and not subRoot: 
          return True
              
        if root and subRoot and root.val == subRoot.val:
          return self.treeCompare(root.left, subRoot.left) and self.treeCompare(root.right,subRoot.right)
                
          return False