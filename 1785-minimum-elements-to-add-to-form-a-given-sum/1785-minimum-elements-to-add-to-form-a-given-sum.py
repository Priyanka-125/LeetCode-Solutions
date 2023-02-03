class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)  
        if s == goal :
            return 0 
        val = abs(goal - s)
        if val <= limit :
            return 1 
        q = val // limit 
        r = val % limit 
        if r == 0 :
            return q 
        return q + 1
        