class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] < nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    
        if nums[0] == '0': 
            return '0' 
       
        
        return ''.join(nums)
        