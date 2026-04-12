class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        sum=0
        for i in operations:
            if i=='+':
                val=stack[-1]+stack[-2]
                stack.append(val)
                sum+=val
            elif i=='D':
                val=2*stack[-1]
                stack.append(val)
                sum+=val
            elif i=='C':
                val=stack.pop()
                sum-=val


            else:
                stack.append(int(i))
                sum+=int(i)
        return sum

        