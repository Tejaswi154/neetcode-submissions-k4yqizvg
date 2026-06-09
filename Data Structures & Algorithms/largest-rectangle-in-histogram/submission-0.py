class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        for i in range(len(heights)):
            left=i
            while(left>=0 and heights[left]>=heights[i]):
                left-=1
            right=i
            while(right<len(heights) and heights[right]>=heights[i]):
                right+=1
            area=((right-left)-1)*heights[i]
            max_area=max(max_area,area)
        return max_area                


        