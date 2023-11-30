class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ''

        for s in strs:
            res += str(len(s)) + '#'+ s

        return res
        # write your code here

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        for i in range(len(str)):
            j = i
            while j != '#':
                j += 1
            
            length = int(str[i:j])

            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

        #Time O(N) Space O(N)