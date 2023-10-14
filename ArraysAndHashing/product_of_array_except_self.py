class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set the positions of the results list with a default value of 1 and a length of the nums list
        res = [1] * (len(nums))

        # iterate over the list of numbers and multiply each number in the results list by the prefix, updating the prefix to be multiplied by the current number we are on.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # iterate backwards and multiply each number in the results list by the postifx, updating the postfix to be multiplied by the current number we are on.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    #Time O(N) - the length of the nums list #Space O(1)


    #Summary: The problem is solved by multiplying the numbers before each index using prefixes, and after using postfixes. 
    # Updating the prefixes and postfixes with the current number to be included for the next position in the results list. It takes 2 loops do to this, one going forwards with pre, one going backwards with post.