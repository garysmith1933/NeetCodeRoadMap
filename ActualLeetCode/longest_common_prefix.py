class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def shortest(stringList):
            smallest = stringList[0]
            for string in stringList:
                if len(string) < len(smallest):
                    smallest = string
            return smallest
        
        min_word = shortest(strs)
        prefixes = []
            
        def prefix(string):
            pfix = ""
            for i in range(len(min_word)):
                char = min_word[i]
                if string[i] != char:
                    return pfix
                pfix += char
            return pfix

        for string in strs:
            prefixes.append(prefix(string))

        return shortest(prefixes)