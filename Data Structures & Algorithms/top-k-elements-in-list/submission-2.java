class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count the freqency of each number
        Map<Integer, Integer> counts = new HashMap<>(); // counts = {1: 1, 2: 2, 3: 3} where num -> count

        for (int num: nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);  // counts = {1=1, 2=2, 3=3}
        }

        // create a list of lists to group numbers by freqency
        // we want freq = [[], [1], [2], [3], [], [], []], given size 6, so freq should be size 7
        List<List<Integer>> freq = new ArrayList<>();
        int size = nums.length + 1;
        for (int i = 0; i < size; i++) {
            freq.add(new ArrayList<>());
        }

        // populate the freq lists
        for (Map.Entry<Integer, Integer> entry: counts.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            freq.get(count).add(num); // freq = [[], [1], [2], [3], [], [], []]
        }

        // collect the top k freq elements
        int[] result = new int[k];
        int index = 0;
        for (int i = freq.size() - 1; i > 0; i--) { // i = 6, 5, 4, ..., 1
            for (int num: freq.get(i)) {
                result[index++] = num; // at the current position, add the num, and then increment the index
                if (index == k) {
                    return result;
                }
            }
        }

        return result;
    }
}
