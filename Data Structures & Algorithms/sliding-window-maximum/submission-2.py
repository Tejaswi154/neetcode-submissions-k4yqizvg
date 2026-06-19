class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        op=[]
        l=0
        max_e=float('-inf')
        for r in range(k-1,len(nums)):
            maxa=max(nums[l:r+1])
            op.append(maxa)
            l+=1

        return op
        