# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        current1 = list1
        current2 = list2

        while current1 and current2:
          if current1.val < current2.val:
            tail.next = current1
            tail = tail.next
            current1 = current1.next
          
          else:
            tail.next = current2
            tail = tail.next
            current2 = current2.next
        
        if current1 == None:
          tail.next = current2
        
        else:
          tail.next = current1
        
        return head.next
    
    # Time O(N + M) Space O( N + M)