class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      # m is the matrix, n is the number of rows
      # iterate over both matrix and rows 
      # at each row, create 2 pointers. Check if the target is within the range of the pointers.
      # if it is not, move on to next row and check there.
      # if it is, check if the target in that row and return if it is found in there or not.

      for m in range(len(matrix)):
        row = matrix[m]
        l, r = 0, len(row) - 1
        if row[l] <= target and row[r] >= target:
            return self.search(row, target)
        else:
          continue
      return False

    def search(self, row:List[int], target: int) -> bool:
      l, r = 0, len(row) - 1
      while l <= r:
        m = (l + r) // 2
        if row[m] > target:
          r = m - 1
        elif row[m] < target:
          l = m + 1  
        else:
          return True
      return False
    
    #Time O(nlog(m * n)) #Space O(1)