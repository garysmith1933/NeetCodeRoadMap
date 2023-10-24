class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      current = head
      prev = None

      while current is not None:
        Next = current.next
        current.next = prev
        prev = current
        current = Next
      
      return prev
        
 #Time O(N) # Space O(1)