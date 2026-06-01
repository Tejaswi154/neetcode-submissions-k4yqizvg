class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        nums_set=set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                len=1
                curr=num
                while curr+1 in nums_set:
                    curr+=1
                    len+=1
                max_len=max(max_len,len)
        return max_len

                
                


            



        
        