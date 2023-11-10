class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while True:
        # if the value of the root is less than both the values of p and q. we dont need to search the left side of the tree where all nodes are less than the root.
            if root.val < p.val and root.val < q.val:
                root = root.right
        # if the value of the root is greater than both the values of p and q. we dont need to search the right side of the tree where all nodes are less than the root.
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # otherwise we found the lca
            else:
                return root
            
            #Time O(Log N) - worst case visit 1 node for every level of the tree  Space O(1)