#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        n=bin(N)
        count=0;maxx=0
        n=n.split("b")[1]
        #print(n)
        for i in range(len(n)):
            if int(n[i])==1:
                count+=1
                maxx=max(maxx,count)
            else:
                count=0
        return maxx





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends