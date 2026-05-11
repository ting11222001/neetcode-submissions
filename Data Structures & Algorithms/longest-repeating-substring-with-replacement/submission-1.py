class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a hashmap to keep track the freq of characters in a substring
        # a substring window is valid only when len(window) - count[s[r]] <= k
        # window size = r - l + 1
        # the max counts in the hashmap = max(counts.values())
        # when the substring window is not valid i.e. replacing counts > k, then shrink the window and update the hashmap

        counts = {}
        res = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)  # in case s[r] is not yet a key in counts
            
            if (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res 