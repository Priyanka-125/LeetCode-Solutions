class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        n=[i for i in str(num)]
        for i in n:
            if num%int(i)==0:
                count+=1
        return count
        