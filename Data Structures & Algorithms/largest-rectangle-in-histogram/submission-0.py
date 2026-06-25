class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][0]:

                h,idx = stack.pop()
                area = h * (i-idx)
                maxArea = max(maxArea, area)

                start = idx

            stack.append((heights[i], start))


        while stack:
            h, idx = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - idx ))

        return maxArea