class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k

        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
          heapq.heappop(self.minheap)

# Time O(n - k  * log n) - N being how many values in list, pop is log n and you would have to call it until the length of the heap is equal is k. worst case O(nlogn)

    def add(self, val: int) -> int:
      heapq.heappush(self.minheap, val)

      if len(self.minheap) > self.k:
        heapq.heappop(self.minheap)

      return self.minheap[0]
      #Time O(logn) Space O(1)
        