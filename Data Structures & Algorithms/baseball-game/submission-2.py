class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        sum=0
        for op in operations:
            if op=="+":
                val=stack[-1]+stack[-2]
                stack.append(val)
                sum+=val
            elif op=='D':
                val=2*stack[-1]
                stack.append(val)
                sum+=val
            elif op=='C':
                removed=stack.pop()
                sum-=removed
            else:
                val=int(op)
                stack.append(val)
                sum+=val
        return sum
                

        