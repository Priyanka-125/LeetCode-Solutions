class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[[]]
        for i in nums:
            output+=[j + [i] for j in output]
        k=set(tuple(i) for i in output) 
        return k
        