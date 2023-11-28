class Solution:
    def search(self, nums: List[int], target: int) -> int:
      l, r = 0, len(nums) - 1

      while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
          return m

        #left sorted portion
        elif nums[m] >= nums[0]:
          #check if it is in range
          if nums[l] <= target and target <= nums[m]:
            r = m - 1
          else:
            l = m + 1
        
        # right sorted portion
        else:
          if nums[m] <= target and target <= nums[r]:
            l = m + 1
          else:
            r = m - 1
      
      return -1
  # Time O(log n) Space O(1)