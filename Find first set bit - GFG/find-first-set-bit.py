#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if n==0:
            return 0
        s=bin(n)
        s=s.split("b")[1]
        #print(s)
        s=s[::-1]
        s=str(s)
        #print(s)
        for i in range(len(s)):
            #print(s[i])
            if s[i]=='1':
                return i+1

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends