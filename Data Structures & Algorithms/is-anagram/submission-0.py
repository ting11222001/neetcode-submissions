class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        for char in s:
            if char not in first:
                first[char] = 0
            first[char] += 1
        
        second = {}
        for char in t:
            if char not in second:
                second[char] = 0
            second[char] += 1
        
        return first == second