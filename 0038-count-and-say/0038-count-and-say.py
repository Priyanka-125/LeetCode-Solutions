class Solution:
    def numsToSay(self,nums):
        s=""
        i=0
        while i<len(nums):
            freq=0
            number=nums[i]
            while i<len(nums) and nums[i]==number:
                i=i+1
                freq=freq+1
            s+=str(freq)+number
        return s
                
    def countAndSay(self, n: int) -> str:
        s="1"
        for i in range(n-1):
            s=self.numsToSay(s)
        return s
            
        