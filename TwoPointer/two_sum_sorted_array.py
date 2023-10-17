class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # set up left and right pointers
        # if the right - left is equal to the target - return the indices + 1 each in a list
        # if the right - left is more than the target, decrease the right
        # if the right - left is less than the target, increase the left.

        left = 0
        right = len(numbers) - 1 

        while True:
          total = numbers[right] + numbers[left]
          if total == target:
            indx1 = left + 1 
            indx2 = right + 1
            return [indx1, indx2]

          if total > target:
            right -= 1
            continue

          else:
            left += 1
            continue

          #Time O(N) Space O(1)