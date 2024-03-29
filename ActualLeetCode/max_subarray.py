# class Solution: #Brute Force
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = nums[0]
#         for i in range(0, len(nums)):
#             curSum = 0
#             for j in range(i, len(nums)):
#                 curSum += nums[j]
#                 maxSum = max(maxSum, curSum)
        
#         return maxSum
#         #Time O(n2) # Space O(1)

class Solution: # Optimal
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        
        return maxSub

    #Time O(N) Space O(1)