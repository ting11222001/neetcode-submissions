class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]
        # Output: 36
        left = 0
        right = len(heights) - 1

        maxArea = 0
        while left < right:
            currArea = abs(right - left) * min(heights[left], heights[right]) # 7 * 1 = 7 -> 6 * 6 = 36 -> 5 * 3 = 15 -> 4 * 7 = 28
            if currArea > maxArea:      # 7 -> 36
                maxArea = currArea
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea

        
        