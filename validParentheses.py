class Solution(object):
    def isValid(self, s):
        d = {")":"(", "]":"[", "}":"{"}
        closed = [")", "]", "}"]
        opened = ["(", "[", "{"]
        
        stack = []
        if len(s)%2!=0:
            return False   
        for i in s:
               if i in opened:
                   stack.append(i)
               elif i in closed:
                  if len(stack)==0:
                     return False
                  elif (stack[-1]!=d[i]):
                      return False
                  else:
                     stack.pop(-1)
        if stack:
             return False
        else:
            return True                  
                      
