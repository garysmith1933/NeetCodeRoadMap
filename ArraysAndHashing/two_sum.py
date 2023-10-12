class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap
        # iterate over list of numbers
        # get the result of subtracting the current from the target, and store it in the map with the indice as the value
        # if the number is in the map, you found the numbers that make the target, return the indices

        #Time O(N) Space O(N)
    
        numbers = {}

        for i in range(len(nums)):
            num = nums[i]
            match = target - num
            if match in numbers: return [ numbers[match], i ] 
            numbers[num] = i