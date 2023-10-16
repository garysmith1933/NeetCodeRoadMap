class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if the string is empty - return true
        # set it up to be lowercase
        # set up two pointers one starting at 0, and the other at the length of the string
        # while the left pointer is less than the right compare them
        #if they are the same - increment the left, decrement the right
        # if they are not return false
        # if the loop breaks without returning false, its a palindrome.
        
        if not s: return true
        s = s.lower()
        left = 0 
        right = len(s) - 1

        alphanum ='abcdefghijklmnopqrsrtuvwxyz0123456789'

        while left <= right:
            if s[left] not in alphanum:
                left += 1
                continue
                
            if s[right] not in alphanum:
                right -= 1
                continue
                
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True

        # Time O(N) # Space O(1)