class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals.sort()
		l=[]
		start=Intervals[0][0]
		end=Intervals[0][1]
		n=len(Intervals)
		if n==1:
		    return Intervals
		for i in range(1,n):
		    s1,e1=Intervals[i-1][0],Intervals[i-1][1]
		    s2,e2=Intervals[i][0],Intervals[i][1]
		    if end>=s2:
		        end=max(e2,end)
		    else:
		        l.append([start,end])
		        start=s2
		        end=e2
		l.append([start,end])
		return l


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends