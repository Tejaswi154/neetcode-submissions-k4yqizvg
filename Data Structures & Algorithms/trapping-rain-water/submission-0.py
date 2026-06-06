class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        for i in range(1,n-1):
            l=max(height[:i])
            r=max(height[i+1:])
            water+=max(0,min(l,r)-height[i])
        return water
        