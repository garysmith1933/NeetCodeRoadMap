class Solution:
    def maxArea(self, height: List[int]) -> int:
      # the max height of 2 points is the shorter height of 2 numbers
      # ex: 8, 7 - the height is 7 because the container would overflow if we went with 8.
      # set up left and right pointer to be first number and last number in array
      # get the length - min between the two heights of the lines
      # get the width - difference between the right pointer and the left.
      # get the area of that container = height * width
      
      maxA = 0
      l, r = 0, len(height) - 1

      while l < r:
        length = min(height[l], height[r])
        width = r - l
        maxA = max(maxA, length * width)

        if height[l] < height[r]:
          l += 1
        
        elif height[r] <= height[l]:
          r -= 1
      
      return maxA

      #Time O(N) #Space O(1)