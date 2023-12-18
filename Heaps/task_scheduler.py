class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time 
        time = 0 
        queue = deque()
        count = Counter(tasks)
        t = [ -cnt for cnt in count.values()] 
        heapq.heapify(t)

        while queue or t:
            time += 1

            if not t: # if heap is empty, set time to what needs to be processed next
                time = queue[0][1]

            else:
                cnt = heapq.heappop(t) + 1

                if cnt: # if the number is not 0, we can process it
                    queue.append([cnt, n + time])
            
            if queue and queue[0][1] == time:
                heapq.heappush(t, queue.popleft()[0])

        return time
        # Time O(N * M) # Space O(N)