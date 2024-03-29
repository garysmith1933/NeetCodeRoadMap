# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         num1Set = set(nums1)
#         res = []

#         for num in nums2:
#             if num in num1Set and num not in res:
#                 res.append(num)
        
#         return res

#         # Time O(n + m)
#         # Space O(n)
  

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        res = []

        for num in nums1:
            count[num] = 1
        
        for num in nums2:
            if num in count and num not in res:
                res.append(num)

        return res

        # Time O(N + M)
        # Space O(N)