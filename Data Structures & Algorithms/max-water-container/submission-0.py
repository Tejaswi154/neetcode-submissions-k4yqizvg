class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        for i in range(len(heights)):
            for j in range(len(heights)):
                water=(j-i)*min(heights[i],heights[j])
                max_water=max(max_water,water)
        return max_water
        