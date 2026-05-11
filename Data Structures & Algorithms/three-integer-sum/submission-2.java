class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Input: nums = [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
        // Output: [[-1,-1,2],[-1,0,1]]

        Arrays.sort(nums); // in-place sorting

        Set<List<Integer>> unique = new HashSet<>();   // Using HashSet to store unique lists

        for (int i = 0; i < nums.length; i++) {
            int j = i + 1;
            int k = nums.length - 1;
            int target = -nums[i];
            while (j < k) {
                if (nums[j] + nums[k] < target) {
                    j++;
                } else if (nums[j] + nums[k] > target) {
                    k--;
                } else {
                    if (!unique.contains(Arrays.asList(nums[i], nums[j], nums[k]))) {
                        unique.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    }
                    j++;
                    k--;
                }
            }
        }

        List<List<Integer>> res = new ArrayList<>(unique);  // Convert the set to a List<List<Integer>>

        return res;

    }
}
