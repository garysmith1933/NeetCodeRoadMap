class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # if we unable to find the target, return -1
      # cut the list in half by finding the middle position
      # if the target is equal to the middle position, we found it
      # if it is greater than the target, check the lower half
      # if it is less, check the upper half.

      # nums = [-1, 4, 5, 7, 11, 34] target = 11 -> output should be 4 because 11 is at index 4
      # nums = [-5, -4 -3, -2, -1] target 0 -> -1 not because it is not in the list of nums.
      l , r = 0, len(nums) - 1

      while l <= r:
        m = (l + r) // 2  

        if nums[m] > target: 
          r = m - 1
        
        elif nums[m] < target:
          l = m + 1
        
        else:
          return m

      return -1 
    
    #Time O(nlogn) #Space O(1)