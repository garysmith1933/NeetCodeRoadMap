class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      # iterate over the tokens
      # if the token is a number, add it to the stack
      # set up cases for when the token is an operation
      # for every case we take the 2 recent numbers from the stack, perform the operation
      # when done, add the result of the operation to the stack.
      # return what is on top of the stack after all operations are done.

      stack = []

      for token in tokens:
          if token == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
          
          elif token == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
          
          elif token == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)
          
          elif token == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(float(num2 / num1)))
         
          else:
            stack.append(int(token))
        
      return stack[-1]