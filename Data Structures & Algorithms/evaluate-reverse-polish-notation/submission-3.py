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
            else:
                stack.append(int(token))

        return stack[0]


        '''
        note: 
        The b // a or int(b) // int(a), the result will always round down (toward negative infinity)
        The b / a operation performs floating-point division, and when you use int() to cast the result, it truncates the decimal part towards zero
       
        e.g. negative numbers
        b = -5
        a = 2
        print(b / a)       # -5 / 2 = -2.5
        print(int(b / a))  # int(-2.5) → -2 (truncates toward zero)

        b = -5
        a = 2
        print(b // a)  # -5 // 2 = -3 (rounds DOWN to next lower integer)

        e.g. positive numbers -> doesn't make much differences here
        b = 5
        a = 2
        print(b / a)       # 5 / 2 = 2.5
        print(int(b / a))  # int(2.5) → 2 (truncates decimal)

        b = 5
        a = 2
        print(b // a)  # 5 // 2 = 2 (already an integer)
        '''