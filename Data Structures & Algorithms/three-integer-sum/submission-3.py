class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,n-1
            while(j<k):
                
                target=-nums[i]
                if target<nums[j]+nums[k]:
                    k-=1
                elif target>nums[j]+nums[k]:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j+=1
                    while j < k and nums[k] == nums[k + 1]:
                    
                        k-=1

                
        return ans

        
        