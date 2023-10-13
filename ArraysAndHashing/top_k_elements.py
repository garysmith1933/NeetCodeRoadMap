class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creates list with the length of the list of nums. each index represents count of how many times a number appears in the list. ex: [1,1] would have 1 be at index 2, because it shows up twice.
        freq = [[] for i in range(len(nums) + 1)]
        # a hash map is created. the keys are the numbers, the values are the number of times they appear in the list.
        count = {}

        for num in nums:
            # if the number has already been accounted for, we increase the number of times it shows, otherwise we set it 1.
            count[num] = 1 + count.get(num, 0)
        
        #iterate over the keys and value from the map.
        for num, num_count in count.items():
            #find the frequency the number appears in the hashmap, and add the number to the list representing the count. ex: if 1 showed up 3 times it would go in the 3rd list in freq, index 3.
            freq[num_count].append(num)
        
        #iterate backwards starting from the last position of freq. add to results until the length of results is the same as k. 
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # Time O(N) # Space O(N)