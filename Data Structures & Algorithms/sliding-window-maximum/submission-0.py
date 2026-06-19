class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        op=[]
        for i in range(len(nums)-k+1):
            max_e=float('-inf')
            for j in range(i,i+k):
                max_e=max(max_e,nums[j])
            op.append(max_e)
        return op
        