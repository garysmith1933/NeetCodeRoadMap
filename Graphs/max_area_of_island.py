class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
      # is the position inbounds - method
      # is the position land 
      # has the position been visited before - set

      def isInbounds(row, col):
        if row < 0 or row == len(grid):
          return False
        if col < 0 or col == len(grid[0]):
          return False
        return True

      def findArea(row, col, visited):
        if not isInbounds(row, col):
          return 0
        
        if grid[row][col] == 0:
          return 0
        
        pos = (row, col)
        if pos in visited:
          return 0
        
        visited.add(pos)
    
        # check left, right, up, down, positions
        return 1 + findArea(row, col + 1, visited) + findArea(row, col - 1, visited) + findArea(row - 1, col, visited) + findArea(row + 1, col, visited) 



      visited = set()
      maxArea = 0

      for r in range(len(grid)):
        for c in range(len(grid[0])):
            maxArea = max(maxArea, findArea(r, c, visited))
      
      return maxArea