class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'I':
                result += 1 if result < 5 else -1
            elif s[i] == 'V':
        	    result += 5
            elif s[i] == 'X':
        	    result += 10 if result < 50 else -10
            elif s[i] == 'L':
        	    result += 50 
            elif s[i] == 'C':
        	    result += 100 if result < 500 else -100
            elif s[i] == 'D':
        	    result += 500
            else:
        	    result += 1000
        return result