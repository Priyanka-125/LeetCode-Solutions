t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l1=[]
    l.sort()
    l=sorted(l,key=l.count,reverse=True)
    print(*l)