class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        print(s)

        for i in range(len(s) - 1, -1, -1):
            word = s[i]
            if len(word) > 0: 
                return len(word)
        