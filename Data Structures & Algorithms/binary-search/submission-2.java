class Solution {
    public int search(int[] nums, int target) {
        // Input: nums = [-1,0,2,4,6,8], target = 4
        // Output: 3

        // nums=[5]
        // target=5
        
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int middle = (left + right) / 2;

            if (target > nums[middle]) {
                left = middle + 1;
            } else if (target < nums[middle]) {
                right = middle - 1;
            } else {
                return middle;
            }
        }
        return -1;
    }
}
