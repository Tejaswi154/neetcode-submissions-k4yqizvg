class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=(len(nums1)+len(nums2))
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2
        l,r=0,len(A)
        while(l<=r):
            i=(l+r)//2
            j=half-i
            Aleft=A[i-1] if i>0 else float("-inf")
            Aright=A[i] if i<len(A) else float("inf")
            j=half-i

            Bleft=B[j-1] if j>0 else float("-inf")
            Bright=B[j] if j<len(B) else float("inf")
            # correct partition
            if Aleft<=Bright and Bleft<=Aright:
                # odd length
                if total%2!=0:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1



    


        
        

        