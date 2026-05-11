class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]
        # Output: 36

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            res = max(res, curr)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res
            