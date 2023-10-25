class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            #increment the count of the letter by 1
            count[s[r]] = 1 + count.get(s[r], 0)
            #while the length of the substring minus the count of the most freq letter is greater than k
            length = r - l + 1
            while length - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, length)
        return res

    # Time O(26N) Space O(N)
