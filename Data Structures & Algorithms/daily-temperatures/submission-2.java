class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        /*
            # Input: temperatures = [30,38,30,36,35,40,28]
            # Output: [1,4,1,2,1,0,0]
            # stack is going to be monotonic decreasing e.g. 73, 72, 71, 71, etc.
        */
        List<List <Integer>> stack = new ArrayList<>();  // stack: [[30, 0], [38, 1], ...]
        int[] result = new int[temperatures.length]; // All elements initialized to 0

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > stack.get(stack.size() - 1).get(0)) {
                int topItemIdx = stack.get(stack.size() - 1).get(1);
                result[topItemIdx] = i - topItemIdx;
                stack.remove(stack.size() - 1);
            }
            stack.add(new ArrayList<>(Arrays.asList(temperatures[i], i)));  
            // stack: [[30, 0]] ->  [[38, 1]] -> [[38, 1], [30, 2]] -> [[38, 1], [36, 3]]
        }

        return result;
    }
}
