class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Input: tokens = ["1","2","+","3","*","4","-"]
        # Output: 5
        # Explanation: ((1 + 2) * 3) - 4 = 5

        # tokens=["4","13","5","/","+"]
        # Output: 6

        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # Output: 22
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop());
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[0]

        '''
        Python Division Operators:
        1. b / a:
        This is true division. It always returns a floating-point result.
        b = 5
        a = 2
        print(b / a)  # Output: 2.5
       
        But in Java, System.out.println(5 / 2);   // Output: 2 (not 2.5, because it's integer division)
        And If You Want Floating-Point Division like Python’s / (returning a float), 
        you need at least one operand to be a floating-point type (double or float):
        System.out.println(5.0 / 2);   // Output: 2.5

        2. b // a:
        This is floor division. It truncates the result to the largest integer less than or equal to the result (essentially, it floors the division result).
        b = 5
        a = 2
        print(b // a)  # Output: 2
        Also, print(-5 // 2)  # Output: -3
        
        But in Java, System.out.println(-5 / 2);  // Output: -2 (truncates toward zero)

        3. int(b / a):
        This first performs true division (b / a) and then casts the result to an integer, effectively truncating the decimal part (similar to rounding down).
        b = 5
        a = 2
        print(int(b / a))  # Output: 2

        4. int(b // a):

        This first performs floor division (b // a), which already returns an integer (no decimal part), and then applies the int() function, 
        which doesn't change anything in this case since the result is already an integer.
        b = 5
        a = 2
        print(int(b // a))  # Output: 2

        '''