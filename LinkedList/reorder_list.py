class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      slow, fast = head, head.next

      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
      second = slow.next 
      slow.next = None
      prev = None
      
      #reverse second half
      while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

      # merge two halfs
      first, second = head, prev
      while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
# Time O(N) Space O(1)