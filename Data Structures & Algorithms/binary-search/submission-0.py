class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Input: nums = [-1,0,2,4,6,8], target = 4
        # Output: 3
        # Tip: the nums array is already sorted
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m       

        return -1