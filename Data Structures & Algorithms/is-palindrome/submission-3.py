class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input: s = "Was it a car or a cat I saw?"
        # Output: true
        # Input: s = "No lemon, no melon" <- it's possible to have two non-alphanumeric characters in a row.
        # Output: true
        # Input: s = "on%@#%no"
        # Output: true
        # Input: s="0P"
        # Output: false

        left = 0
        right = len(s) - 1
        s = s.lower()  # just realize 'W' != 'w'

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1      
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True  # i.e. when left == right