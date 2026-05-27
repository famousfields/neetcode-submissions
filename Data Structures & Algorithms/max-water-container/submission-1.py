class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        for i in range(len(heights)-1):
            j = i+1
        
            while j < len(heights):
                if heights[i] >= heights[j]:
                    maxWater = max(maxWater,(j-i) * heights[j])
                else:
                    maxWater = max(maxWater,(j-i) * heights[i])

                j += 1

        return maxWater

        