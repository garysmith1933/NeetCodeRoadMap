class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       # split list into two halfs
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next # the beginning of the second half once the fast pointer reaches the end.
        prev = slow.next = None 

        while second_half: # reverse second half
           temp = second_half.next
           second_half.next = prev
           prev = second_half
           second_half = temp
        # the prev pointer is the beginning of the new second half.

        first, second = head, prev
        while second: # merge two halfs
           temp1, temp2 = first.next, second.next
           first.next = second
           second.next = temp1

           first, second = temp1, temp2 