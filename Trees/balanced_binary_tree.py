class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

      #create a function to return something other than the boolean
      def dfs(root):
        if not root: return [True, 0]

        #checks if the children are balanced subtrees
        left, right = dfs(root.left), dfs(root.right)
        
        # if one of them are false, the whole thing is false
        # otherwise, check if the height difference between the children are greater than or  equal to 1
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        # return if its balanced, and the height of it plus its children
        return [balanced, 1 + max(left[1], right[1])]
      
      return dfs(root)[0]
      #Time O(N) Space O(N)