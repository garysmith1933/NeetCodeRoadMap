class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        
        res = 0
        idx = 0

        while idx < len(s):
            char1, char2 = s[idx], s[idx + 1] if idx + 1 != len(s) else ""
        
            potential_num = char1 + char2

            if potential_num in roman_to_int:
                res += roman_to_int[potential_num]
                idx += 2
            
            else:
                if char1 in roman_to_int:
                    res += roman_to_int[char1]
                    idx += 1

        return res