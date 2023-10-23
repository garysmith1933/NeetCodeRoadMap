class Solution:
    def isValid(self, s: str) -> bool:
      # stores the open/close brackets in a dict
      Map = {
      ")":"(", 
      "}":"{", 
      "]":"["
      }

      stack = []

      for char in s:
        # if it is an opening, add it to the stack. 
        # The stack should ONLY have OPENING parenthesis
        if char not in Map:
          stack.append(char)
          continue
      
      # if the char is a closing parenthesis, but the stack is empty OR 
      # if the most recent opening parenthesis in the stack is NOT mapped 
      # to the closing parenthesis that we are on, its not valid.
        if not stack or stack[-1] != Map[char]:
          return False

        stack.pop()
      
      # is there anything that hasnt been taken care of
      return not stack

      # Time O(N) # Space O(N)