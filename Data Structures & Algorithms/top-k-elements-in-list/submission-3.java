class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count the freqency of each number
        Map<Integer, Integer> counts = new HashMap<>(); // counts = {1: 1, 2: 2, 3: 3} where num -> count

        for (int num: nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);  // counts = {1=1, 2=2, 3=3}
        }
        
        // create an array of int[]
        List<int[]> arr = new ArrayList<>(); // We want arr = [[1, 1], [2, 2], [3, 3]...]
        for (Map.Entry<Integer, Integer> entry: counts.entrySet()) {
            int count = entry.getValue();
            int num = entry.getKey();
            arr.add(new int[] {count, num});
        }

        arr.sort((a, b) -> b[0] - a[0]); 
        // a and b are two elements (both int[] in this case) 
        // b[0] - a[0] calculates the difference between the first element of b and the first element of a
        // if positive, it will sort in descending order

        // So, arr = [[3, 3], [2, 2], [1, 1]] where [[count, num],...]
        // To print it:
        /*
            for (int[] item: arr) {
                System.out.println(Arrays.toString(item));
            }
        */

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = arr.get(i)[1];
        }

        return result;
    }
}
