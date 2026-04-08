class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1

        while l<r:
            abs_height = min(heights[l], heights[r])
            res = max(res, (abs_height*(r-l)))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return res
        