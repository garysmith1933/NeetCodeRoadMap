class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # is the string all lowercase characters? if not should they be considered the same?
        # do we have to worry about any whitespace?
        # would we just move the pointers together???

        res = 0 
        seen = set()
        l = 0 

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - 1 + 1 # cancels out O based indexing
            res = max(res, length)
            r += 1
        return res

        # Time O(N) Space O(N)