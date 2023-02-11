class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')':
                if len(stack)==0:
                    count+=1
                else:
                    top=stack.pop()
                    if i is ')' and top is not '(':
                        count+=1
        if len(stack)!=0:
            count+=len(stack)
        return count
        