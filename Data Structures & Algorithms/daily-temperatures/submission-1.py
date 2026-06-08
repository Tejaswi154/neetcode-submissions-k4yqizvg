class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op=[]
        n=len(temperatures)
        
        for i in range(n):
            found=False
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    op.append(j-i)
                    found=True
                    break
            if not found:
                op.append(0)
                
        
        return op
                
        