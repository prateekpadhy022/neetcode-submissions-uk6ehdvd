class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while l<r:
            if heights[l]< heights[r]:
                area = heights[l] * (r-l)
                l += 1
            elif heights[l]>heights[r]:
                area = heights[r] * (r-l)
                r -= 1
            else:
                area = heights[l] * (r - l)
                l += 1
            if area>res:
                res = area
        return res
        
