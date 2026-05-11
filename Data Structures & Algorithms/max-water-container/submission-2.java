class Solution {
    public int maxArea(int[] heights) {
        // Input: height = [1,7,2,5,4,7,3,6]
        // Output: 36

        int res = 0;
        int l = 0;
        int r = heights.length - 1;

        while (l < r) {
            int curr = (r - l) * Math.min(heights[l], heights[r]);
            res = Math.max(curr, res);

            if (heights[l] > heights[r]) {
                r--;
            } else {
                l++;
            }
        }

        return res;
    }
}
