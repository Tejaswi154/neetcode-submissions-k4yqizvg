class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp={}
        for i,num in enumerate(numbers):
            need=target-num
            if need in mp:
                return [mp[need]+1,i+1]
            mp[num]=i


        
        
                
                
            


        