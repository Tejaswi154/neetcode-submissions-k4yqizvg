class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs=set()
        for i in range(len(nums)):
            if nums[i] in hs:
                return nums[i]
            hs.add(nums[i])
        
        