class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        right=[0]*n
        left=[0]*n
        water=0
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        for i in range(n):
            water=water+min(left[i],right[i])-height[i]
        return water