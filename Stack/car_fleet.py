class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      stack = []
      #zip the speed and positions for the cars into one list.
      pair = [(p,s) for p,s in zip(position, speed)]
      pair.sort(reverse=True) # reverse sorted order
      for p, s in pair:
        carTravelTime = (target - p) / s
        stack.append(carTravelTime)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
          stack.pop()
        
      return len(stack)

      #Time O(N) Space O(N)
