class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n + m)
        Space complexity: O(n + m)
        where n is the length of the string s and m is the length of the string t.
        """
        
        """
        Return False when string lengths are different.
        """
        if len(s) != len(t):
            return False
        
        """
        Now both strings have the same length.
        Create hash maps for each string.
        Take each character in the string and add to the map.
        Increment the count by 1. Default 0 when creating the key to the map.
        Compare the each map's key and see if the counts of the character is the same.
        Include the case where countT map doesn't have the character as countS.
        """
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

