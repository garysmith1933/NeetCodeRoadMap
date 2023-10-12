class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Iterate over the first string 
        # Add each one to the hashmap with how many times it appears

        # iterate the second one
        # if the letter is not in the dictionary, false
        # if it is, check if the count is 0, if it is, false
        # otherwise, decrement by 1 '''

        # iterate over the map - has every letter been used?
        # if the value of any of the letters is not 0, its false because something wasnt used

        # if it passes all this, its a anagram
        # Time O(N) Space O(N)
        
        if len(s) != len(t): return False

        wordBank = {}

        for char in s:
            if char not in wordBank:
                wordBank[char] = 0;
            
            wordBank[char] += 1
        
        for char in t:
            if char not in wordBank: return False
            if wordBank[char] == 0: return False
            wordBank[char] -= 1
        
        for char in wordBank:
            if wordBank[char] is not 0: return False
        
        return True
        