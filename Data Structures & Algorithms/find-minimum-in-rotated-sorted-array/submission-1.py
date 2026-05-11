class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given a sorted array and aiming for O(log n) time
        # trying to find the min value but the pivot value can be anywhere:
        # if the nums[mid] belongs to the right sorted portion, then go left (coz to its right, the value will only get bigger)
        # if the nums[mid] belongs to the left sorted portion, then go right

        # if nums[mid] >= nums[left]
        # then search right
        # else search left

        # Input: nums = [3,4,5,6,1,2]
        # Input: nums = [4,5,0,1,2,3]
        # Edge case: nums = [4,5,6,7,0,1,2]


        left = 0
        right = len(nums) - 1
        res = nums[0]  # res has to be initialized to be a valid local variable to be returned at the end (random value)

        while left <= right:
            if nums[left] < nums[right]:   # if we're in a sorted portion already, the leftmost value will always be the smallest (edge case)
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1      # if mid value > left value, then it belongs to the left, so go right
            else:
                right = mid - 1

        return res
        