class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      # is the position inbounds - method
      # is the position land 
      # has the position been visited before - set

      def isInbounds(row, col):
        if row < 0 or row >= len(grid):
          return False
        if col < 0 or col >= len(grid[0]):
          return False
        return True

      def findArea(row, col, visited):
        if not isInbounds(row, col):
          return False
        
        if grid[row][col] == "0":
          return False
        
        pos = (row, col)
        if pos in visited:
          return False
        
        visited.add(pos)
    
        # check left, right, up, down, positions
        findArea(row, col + 1, visited) # right
        findArea(row, col - 1, visited) # left
        findArea(row - 1, col, visited) # up
        findArea(row + 1, col, visited) # down

        return True


      visited = set()
      islands = 0

      for r in range(len(grid)):
        for c in range(len(grid[0])):
          if findArea(r, c, visited):
            islands += 1
  
      
      return islands
# Time O(r * c) Space O(N)
  