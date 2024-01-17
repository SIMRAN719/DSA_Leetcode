class Solution(object):
    def isValid(self, s):
        stack=[]
        top=-1
        for i in s:
            if (i=='(' or i=='[' or i=='{'):
                stack.append(i)
                top+=1
            elif ((i==']' or i==")" or i=='}')and stack==[]):
                return False
            elif ((i==']' and stack[top]=='[') or (i==")" and stack[top]=="(") or (i=='}' and stack[top]=='{')):
                stack.pop()
                top-=1
            else:
                return False
        b=bool(stack)
        a=not b
        return a