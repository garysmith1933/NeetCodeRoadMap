class Solution: #Brute Force
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(0, len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        
        return maxSum
        #Time O(n2) # Space O(1)