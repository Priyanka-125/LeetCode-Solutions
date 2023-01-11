
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        '''
        res = 0
  
        # For every element of the array
        for i in range(1, n - 1):
      
            # Find the maximum element on its left
            left = arr[i]
            for j in range(i):
                left = max(left, arr[j])
      
            # Find the maximum element on its right
            right = arr[i]
      
            for j in range(i + 1, n):
                right = max(right, arr[j])
      
            # Update the maximum water
            res = res + (min(left, right) - arr[i])
      
        return res
        '''
        left = [0]*n
  
        # Right [i] contains height of tallest bar to
        # the right of ith bar including itself
        right = [0]*n
      
        # Initialize result
        water = 0
      
        # Fill left array
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
      
        # Fill right array
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
        for i in range(0, n):
            water += min(left[i], right[i]) - arr[i]
      
        return water
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends