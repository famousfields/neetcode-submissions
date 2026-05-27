class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [7,1,7,2,2,4]
         
        """

        maxA = heights[0]
        stack = []


        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxA = max(maxA, height*(i-index))
                start = index
            stack.append((start,h))

        for i,h in stack:
            maxA = max(maxA, h *(len(heights)-i))
        return maxA


        