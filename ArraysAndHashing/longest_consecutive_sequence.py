class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       # start with set of the nums list
        numSet = set(nums)
        # set longest variable to 0
        longest = 0
       # iterate over the nums set
        for n in numSet:
              #if the current number - 1 is not in the set we can start counting
            if (n - 1) not in numSet:
                  #set the length of it to 1
                length = 1
                # while the current number + the length is in the set - is the number afterwards in the set
                while (n + length) in numSet:
                     # increment the length
                    length += 1
                  # when it breaks, compare the length of it, to the current longest length. assign it to which is more.
                longest = max(longest, length)
        return longest
    #Time O(N) Space O(1)
    
    