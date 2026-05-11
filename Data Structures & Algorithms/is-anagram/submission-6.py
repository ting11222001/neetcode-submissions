class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Python's sorted() uses Timsort, which is O(k log k) where k is the length of the input. So sorting s is O(n log n) and sorting t is O(m log m), giving a total of O(n log n + m log m).
        """
        return sorted(s) == sorted(t)