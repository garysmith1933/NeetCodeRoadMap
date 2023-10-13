class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, num_count in count.items():
            freq[num_count].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # Time O(N) # Space O(N)