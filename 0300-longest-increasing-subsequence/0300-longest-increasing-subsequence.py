class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                print(j)
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    print(dp)

        return max(dp)
        '''
        ans = [nums.pop(0)]         # use this list to track increasing
        
        for num in nums:            # add current number into the list
            if num > ans[-1]:
                ans.append(num)
            else:
                ans[bisect_left(ans, num)] = num
                print(ans)
        return len(ans)