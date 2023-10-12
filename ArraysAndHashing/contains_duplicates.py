class Solution(object):
    ''' Time O(N) Space O(N) '''
    def containsDuplicate(self, nums):
        ''' Making a set will remove duplicates, comparing its length to the length of the original list will 
        see if there are any duplicates '''
        return not len(set(nums)) == len(nums)
        