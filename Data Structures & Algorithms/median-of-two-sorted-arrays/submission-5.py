class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=(len(nums1)+len(nums2))
        n=total//2
        i,j=0,0
        prev=0
        curr=0
        counter=0
        while(counter<=n):
            if i<len(nums1) and (j>=len(nums2) or nums1[i]<nums2[j]):
                prev=curr
                curr=nums1[i]
                i+=1
            else:
                prev=curr
                curr=nums2[j]
                j+=1
            counter+=1
        if total%2!=0:
            return curr
        else:
            return (curr+prev)/2
    


        
        

        