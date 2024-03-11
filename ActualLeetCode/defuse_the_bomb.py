class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        temp = code 
        code = code * 2

        for i in range(len(temp)):
            if k > 0:
                start = i + 1
                end = i + k + 1
                temp[i] = sum(code[start:end])
            
            else:
                start = i + len(temp) + k
                end = i + len(temp)
                temp[i] = sum(code[start : end])
            
        return temp
  
  # Time O(n * k) #Space O(n)