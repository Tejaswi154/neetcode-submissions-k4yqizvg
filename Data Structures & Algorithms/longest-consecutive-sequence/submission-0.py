class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        for num in nums:
            len=1
            current=num
            while current+1 in nums:
                current+=1
                len+=1
            max_len=max(max_len,len)
        return max_len

                
                


            



        
        