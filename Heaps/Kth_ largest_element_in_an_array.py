class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [ num * -1  for num in nums ] # [ -5 , -3, -1, 4, 5, ,6] -> [ -6, -5, -4, 1, 3, 5]
        heapq.heapify(nums)
    
        i = 0
        while i < k:
            value = heapq.heappop(nums)
            i += 1
            if i == k:
                return value * -1  # multiply by -1 