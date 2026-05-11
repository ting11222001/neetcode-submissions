class Solution {
    public int findMin(int[] nums) {
        // 3,4,5,1,2: if nums[m] >= nums[l], then part of left, so search right
        // 5,0,1,2,3: if nums[m] < nums[l], so everthing to the right is big, so search left

        int left = 0;
        int right = nums.length - 1;
        int res = nums[0];

        while (left <= right) {
            if (nums[left] < nums[right]) {     // when m = 1 in this example: 3,4,5,1,2
                res = Math.min(res, nums[left]);
                break;
            }

            int mid = (left + right) / 2;
            res = Math.min(res, nums[mid]);

            if (nums[mid] >= nums[left]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return res;
    }
}
