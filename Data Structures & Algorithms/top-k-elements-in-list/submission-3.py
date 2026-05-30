class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls=[]
        freq={} 
        
        for i in nums:
            freq[i]=freq.get(i,0)+1
        buckets=[]
        for _ in range(len(nums)+1):
            buckets.append([])
    

        for num,count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                ls.append(num)
                if len(ls)==k:
                    return ls
        
        

            
               
        

        
        