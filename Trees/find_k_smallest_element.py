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
    
    #Time O(N * Log(N)) Space O(N) - BRUTE FORCE


    # class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #  n = 0
    #  stack = []
    #  curr = root

    #  while stack or curr:
    #     while curr:
    #         stack.append(curr)
    #         curr = curr.left
    #     curr = stack.pop()
    #     n+=1
    #     if n == k:
    #         return curr.val
    #     curr = curr.right

    #     #Time O(N) #Space O(1) - OPTIMAL