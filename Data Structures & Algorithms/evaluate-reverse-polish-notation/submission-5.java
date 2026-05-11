class Solution {
    public int evalRPN(String[] tokens) {
        /** 
        # Input: tokens = ["1","2","+","3","*","4","-"]
        # Output: 5
        # Explanation: ((1 + 2) * 3) - 4 = 5

        # tokens=["4","13","5","/","+"]
        # Output: 6

        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # Output: 22
        **/

        Stack<Integer> stack = new Stack<>();

        for (String token: tokens) {
            if (token.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (token.equals("-")) {
                int right = stack.pop();
                int left = stack.pop();
                stack.push(left - right);
            } else if (token.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (token.equals("/")) {
                int right = stack.pop();
                int left = stack.pop();
                stack.push(left / right);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();

        // In Java, == compares object references, not the actual contents of strings. Since token is a String, you should use .equals() instead
    }
}
