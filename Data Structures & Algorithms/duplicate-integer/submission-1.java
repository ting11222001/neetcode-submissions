class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int num: nums) {
            if (!counts.containsKey(num)) {
                counts.put(num, 0);
            }
            counts.put(num, counts.get(num) + 1);
            if (counts.get(num) > 1) {
                return true;
            }
        }
        return false;
    }
}
