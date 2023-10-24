class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        num1 = ""

        current2 = l2
        num2 = ""

        while current1 is not None:
          num1 += str(current1.val)
          current1 = current1.next
  
        while current2 is not None:
          num2 += str(current2.val)
          current2 = current2.next
      
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])

        total = str(num1 + num2)
        total = total[::-1]
        print(total)

        head = ListNode(0)
        tail = head

        for i in range(0, len(total)):
          tail.next = ListNode(total[i])
          tail = tail.next
          
        
        return head.next