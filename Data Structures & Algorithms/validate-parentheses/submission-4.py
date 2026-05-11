class Solution:
    def isValid(self, s: str) -> bool:
        # Input: s = "[]" Output: true
        # Input: s = "([{}])" Output: true
        # Input: s = "[(])" Output: false

        # Edge cases:
        # Input: s="]]" Output: false
        # Input: s="]" Output: false
        # Input: s="(){}}{" Output: false
        # Input: s="[" Output: false

        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in brackets:  # closing
                if stack and stack[-1] == brackets[c]:  # if stack is not empty and the top val can be a pair
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) > 0:
            return False
        else:
            return True
                    


