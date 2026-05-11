class Solution {
    public int[] productExceptSelf(int[] nums) {
        // nums: [1,2,3,4]
        // output 1st pass: [1,1,2,6]
        // output 2nd pass: [24,12,8,6]
        int n = nums.length;
        int[] res = new int[n];
        int pref = 1;
        int post = 1;

        for (int i = 0; i < n; i++) {
            res[i] = pref;
            pref = nums[i] * pref; 
        }

        for (int i = n - 1; i >= 0; i--) {
            res[i] = post * res[i];
            post = nums[i] * post;
        }

        return res;
    }
}  
