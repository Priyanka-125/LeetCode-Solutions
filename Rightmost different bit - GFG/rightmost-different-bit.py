#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        m=bin(m)
        n=bin(n)
        m=m.split("b")[1]
        n=n.split("b")[1]
        l=0
        if m==n:
            return -1
        m=m[::-1]
        n=n[::-1]
        if m=='0':
            for i in range(len(n)):
                if n[i]=='1':
                    return i+1
        elif n=='0':
            for i in range(len(m)):
                if m[i]=='1':
                    return i+1
        elif len(m)>=len(n):
            l=len(n)
        else:
            l=len(m)
        for i in range(l):
            if m[i]!=n[i]:
                return i+1
        return i+2
                
                
'''         
m=bin(m)[2:]
        n=bin(n)[2:]
        if m==n:
            return -1
        m=m[::-1]
        n=n[::-1]
        if m=='0':
            for i in range(len(n)):
                if n[i]=='1':
                    return i+1
        elif n=='0':
            for i in range(len(m)):
                if m[i]=='1':
                    return i+1
        elif len(m) > len(n):
            length = len(n)
        else:
            length = len(m)
        count = 0
        # m=m[::-1]
        # n=n[::-1]
        for i in range(length):
            if m[i]!=n[i]:
                return i+1
        return i+2
        '''

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends