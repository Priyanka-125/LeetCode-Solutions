class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)

                case ')' | ']' | '}':
                    if len(stack) is 0:
                        return False
                    
                    top = stack.pop()
  
                    if c is ')' and top is not '(':
                        return False
                    
                    elif c is ']' and top is not '[':
                        return False
                    
                    elif c is '}' and top is not '{':
                        return False

                case _:
                    return False
        
        if len(stack) is not 0:
            return False

        return True
        