from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            #list containing positions for the 26 letters lowercased
            char_count = [0] * 26
            for char in word:
                #maps the letters to the positions in the list. 
                # ex: unicode a is 97. b is 98. 98 - 97 = 1. b is at index 1.
                # we add 1 to the letters position in the list to count how many times it appears.
                char_count[ord(char) - ord("a")] += 1
            
            # lists cannot be keys in a dict, so we convert it to a tuple.
            res[tuple(char_count)].append(word)
        return res.values()
        

        #Time O(N * M) N - the number of strings in the list, M - the average length of each string
        #Space O(N)