class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> diffs = new HashMap<>();  // val -> index

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (diffs.containsKey(diff)) {
                return new int[] {diffs.get(diff), i};
            }
            diffs.put(num, i); 
        }

        return new int[] {};
    }
}
