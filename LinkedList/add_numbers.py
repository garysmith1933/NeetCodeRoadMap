class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        #while either list has numbers or a carry still exists after computing the numbers from the list
        while l1 or l2 or carry:
          #check if the numbers are present, if one is null give it a default of -
          v1 = l1.val if l1 else 0
          v2 = l2.val if l2 else 0

          #calculate the sum of the current numbers, if its over 10
          val = v1 + v2 + carry
          print(carry, carry // 10)
          # if the value is 15, the carry is 1, 15 goes into 10 1 time
          carry = val // 10
          # if the value is 15, after this it is 5 since 5 is left over after 15 goes into 10
          val = val % 10

          cur.next = ListNode(val)
          cur = cur.next

          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None
        
        return dummy.next
    
    # Time O(max(N, M) # Space O(max(N, M))
