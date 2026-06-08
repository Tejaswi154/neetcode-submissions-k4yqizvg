class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op=[]
        
        for i in range(len(temperatures)):
            found=False
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    op.append(j-i)
                    found=True
                    break
            if not found:
                op.append(0)
                
        
        return op
                
        