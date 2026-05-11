class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Input: [3,4,5,6,1,2], target = 1
        # Output: 4

        # Input: [4,5,6,7,0,1,2], target = 4
        # Output: 0

        # Input: [1,3], target = 3
        # Output: 1

        # Input: [5,1,3], target = 5
        # Output: 0

        # Start with finding out if the mid is in the left or right portion of the array

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # if mid is in the left portion, use the leftmost value to decide which direction to go
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # if mid is in the right portion, use the rightmost value to decide which direction to go
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1