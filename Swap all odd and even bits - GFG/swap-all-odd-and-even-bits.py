#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        s=""
        n=bin(n)
        n=n.split("b")[1]
        l=len(n)
        if(l%2==1):
           n="0"+n
        s=""
        for i in range(0,l,2):
            s+=n[i+1]
            s+=n[i]
        return int(s,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends