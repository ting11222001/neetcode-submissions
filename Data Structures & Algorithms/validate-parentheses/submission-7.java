class Solution {
    public boolean isValid(String s) {
        // Input: s = "[]" Output: true
        // Input: s = "([{}])" Output: true
        // Input: s = "[(])" Output: false
        // Input: s="]]" Output: false
        // Input: s="]" Output: false
        // Input: s="(){}}{" Output: false
        // Input: s="[" Output: false

        Map<Character, Character> brackets = new HashMap<>();  // close to open brackets
        brackets.put(')', '(');
        brackets.put(']', '[');
        brackets.put('}', '{');

        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()) {
            if (brackets.containsKey(c)) {      // c is closing bracket
                if (!stack.isEmpty() && brackets.get(c) == stack.peek()) {
                    stack.pop();
                } else {
                    return false;
                }   
            } else {                            // c is open bracket
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
