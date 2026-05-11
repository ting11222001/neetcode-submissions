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
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))  
                # note: 
                # The b // a or int(b) // int(a), the result will always round down (toward negative infinity)
                # The b / a operation performs floating-point division, and when you use int() to cast the result, it truncates the decimal part towards zero

            else:
                stack.append(int(token))

        return stack[0]