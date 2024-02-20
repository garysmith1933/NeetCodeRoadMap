class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = nums[0]

        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        for num in count:
            if count[num] > count[majority]:
                majority = num
        
        return majority