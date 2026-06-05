class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            j,k=i+1,n-1
            while(j<k):
                target=-nums[i]
                if target<nums[j]+nums[k]:
                    k-=1
                elif target>nums[j]+nums[k]:
                    j+=1
                else:
                    aa=tuple(sorted([nums[i],nums[j],nums[k]]))
                    ans.add(aa)
                    j+=1
                    k-=1

                
        return [list(x) for x in ans]

        
        