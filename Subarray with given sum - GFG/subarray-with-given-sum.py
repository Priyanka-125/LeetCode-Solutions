#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        currwindowsum=0
        low=0
        high=0
        li=[]
        for high in range(0,n):
            
            currwindowsum+=arr[high]
            while currwindowsum>s and low<high:
                currwindowsum-=arr[low]
                low+=1
            
            if currwindowsum==s:
                li.append(low+1)
                li.append(high+1)
                return li
            
        return [-1]        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends