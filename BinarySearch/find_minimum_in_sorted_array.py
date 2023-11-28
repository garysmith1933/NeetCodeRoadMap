class Solution:
    def findMin(self, nums: List[int]) -> int:
      l, r = 0, len(nums) - 1
      res = nums[0]

      while l <= r:
        m = (l + r) // 2

        if nums[l] < nums[r]:
          res = min(res, nums[l])
          break

        res = min(res, nums[m])
        # is the middle number part of the left side that is sorted?
        if nums[m] >= nums[l]:
          # if it is part of the left side, check the right
          l = m + 1
        
        else:
          # if it is not, check the left side
          r = m - 1
      
      return res
      
      # Time O(log n) Space O(1)