class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      answers = [0] * len(temperatures)
      stack = []

      for idx, val in enumerate(temperatures):
        while stack:
          stackIdx, stackTemp = stack[-1]
          if val > stackTemp:
            daysSince = idx - stackIdx
            answers[stackIdx] = daysSince
            stack.pop()
          
          else:
            break
        
        stack.append((idx, val))
      return answers

      #Time O(N) #Space O(N)
