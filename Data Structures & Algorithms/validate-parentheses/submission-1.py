class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]  
        mapping={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in s:
            if i in mapping: # for closing bracket
                if not stack or stack[-1]!=mapping[i]:
                    return False
                stack.pop()
            else:  # if it is an opening bracket
                stack.append(i)
        return  len(stack)==0
