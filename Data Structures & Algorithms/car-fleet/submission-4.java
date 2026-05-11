class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        /*
        # time to reach target = (target position - curr position) / curr speed
        # keep the slow car and see it as a fleet
        # start from the right i.e. start from the car that's closest to the target

        # Input: target = 10, position = [1,4], speed = [3,2] Output: 1 
        # Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1] Output: 3
        */

        List<List<Integer>> pairs = new ArrayList<>();
        for (int i = 0; i < position.length; i++) {
            pairs.add(Arrays.asList(position[i], speed[i]));
        }

        pairs.sort((a, b) -> Integer.compare(b.get(0), a.get(0)));

        System.out.println(pairs);

        Stack<Double> stack = new Stack<>();
        for (int i = 0; i < pairs.size(); i++) {
            double currTime = (double) (target - pairs.get(i).get(0)) / pairs.get(i).get(1);    // put (double) on one operand!
            stack.push(currTime);
            if (stack.size() >= 2 && stack.get(stack.size() - 1) <= stack.get(stack.size() - 2)) {
                stack.pop();
            }
        }

        System.out.println(stack);

        return stack.size();
    }
}

/*
Use (double) on at least one operand for floating-point division.

e.g.
target=10
position=[6,8]
speed=[3,2]
pairs=[[8, 2], [6, 3]]

At the line of "currTime":
When double result = (10 - 6) / 3;
10 - 6 → 4 (integer).
4 / 3 is integer division because both 4 and 3 are integers.
Java truncates (removes) the decimal part, so 4 / 3 becomes 1.
Result: 1.0 (Wrong if you expected 1.3333)

When double result = (double) (10 - 6) / 3;
(10 - 6) → 4 (integer).
(double) 4 converts 4 into 4.0.
4.0 / 3 → floating-point division → 1.3333.
Result: 1.3333

When double result = (10 - 6) / (double) 3;
10 - 6 is integer subtraction → 4 (still an integer).
(double) 3 converts 3 into 3.0, making the division:
4 / 3.0 → floating-point division → 1.3333.
Result: 1.3333
*/
