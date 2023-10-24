class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using a set to keep track of the nodes that we have visited.
        # when we are traversing through the nodes, we can check if it is in our set.
        # if it is, its a cycle.
        # add each node to set
        # if we break out the loop without reaching a cycle return false

        visited = set()

        while head is not None:
          if head in visited: return True
          visited.add(head)
          head = head.next
        
        return False

        # Time O(N) Space O(N) 