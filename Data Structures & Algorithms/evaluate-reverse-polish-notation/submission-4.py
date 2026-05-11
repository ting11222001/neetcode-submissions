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
        # The b // a or int(b) // int(a), the result will always round down (toward negative infinity).
        // in Python is used for integer division, also known as floor division. 
        It divides two numbers and rounds the result down to the nearest integer, toward negative infinity.
        
        # The b / a operation performs floating-point division, and when you use int() to cast the result, it truncates the decimal part towards zero
       

       
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


        For example, to add 3 and 4 together, the expression is 3 4 + rather than 3 + 4. 
        The conventional notation expression 3 − 4 + 5 becomes 3 (enter) 4 − 5 + in reverse Polish notation: 
        4 is first subtracted from 3, then 5 is added to it.
        The concept of a stack, a last-in/first-out construct, is integral to the left-to-right evaluation of RPN. 
        In the example 3 4 −, first the 3 is put onto the stack, then the 4; the 4 is now on top and the 3 below it. 
        The subtraction operator removes the top two items from the stack, performs 3 − 4, and puts the result of −1 onto the stack.
        '''