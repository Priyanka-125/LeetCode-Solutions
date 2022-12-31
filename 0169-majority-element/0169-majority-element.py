class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        big=[]
        z=0
        for i in set(nums):
            if nums.count(i) > len(nums)//2:
                return i