class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair [temp, index]

        for i, t in enumerate(temperatures):
          # if the temperature of the current number is higher 
          #than the temp at the top of our stack
          while stack and t > stack[-1][0]:
            stackTemp, stackIdx = stack.pop()
            # we get the index and set its position in the results to be 
            # the difference between the current index and its index 
            # to represent how many days it has been since a higher temp than that day.
            res[stackIdx] = i - stackIdx

          stack.append([t, i])
        return res
    #Time O(N) #Space O(N)
