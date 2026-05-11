class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        /*
        # time to reach target = (target position - curr position) / curr speed
        # keep the slow car and see it as a fleet
        # start from the right i.e. start from the car that's closest to the target

        # Input: target = 10, position = [1,4], speed = [3,2] Output: 1 
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1] Output: 3
        */

        // make pairs
        List<List<Integer>> pairs = new ArrayList<>();
        for (int i = 0; i < position.length; i++) {
            pairs.add(Arrays.asList(position[i], speed[i]));
        }
        // pairs: [[1, 3], [4, 2]]

        pairs.sort((a, b) -> Integer.compare(b.get(0), a.get(0)));
        // pairs: [[4, 2], [1, 3]]

        System.out.println(pairs);

        // make a stack to save the calculated time
        Stack<Double> stack = new Stack<>();    // Use Floating-Point Division
        for (int i = 0; i < pairs.size(); i++) {
            double currTime = (double) (target - pairs.get(i).get(0)) / (double) pairs.get(i).get(1);
            stack.push(currTime);
            if (stack.size() >= 2 && stack.get(stack.size() - 1) <= stack.get(stack.size() - 2)) {   // pop the slow, new one
                stack.pop();
            }
        }

        System.out.println(stack);

        return stack.size();
    }
}
