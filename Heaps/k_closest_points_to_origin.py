class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        origin = 0
        distances = []

        for point in points:
            x, y = point
            distance = (x - 0) ** 2 + (y - 0) ** 2
            distances.append([ distance, point])
        
        heapq.heapify(distances)

        while len(res) != k:
            coordinate = heapq.heappop(distances)
            res.append(coordinate[1])

        return res 

        #Time O(n logn ) # Space O(N)