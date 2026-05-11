class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Input: s1 = "abc", s2 = "lecabee"
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26        
        s2_counts = [0] * 26

        # the 1st round   
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1   # s1_counts = [1, 1, 1, 0....]
            s2_counts[ord(s2[i]) - ord('a')] += 1   # s2_counts = [0, 0, 1, 0, 1 ... 1, 0, 0....]

        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
            else:
                matches += 0

        s1_length = len(s1)
        L = 0

        # the right pointer starts from the 2nd round
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # when adding one new character from the Right into the window
            index = ord(s2[R]) - ord('a')
            s2_counts[index] += 1
            if s1_counts[index] == s2_counts[index]:
                matches += 1
            elif s1_counts[index] + 1 == s2_counts[index]:
                matches -= 1

            # when removing one new character from the Left from the window
            index = ord(s2[L]) - ord('a')
            s2_counts[index] -= 1
            if s1_counts[index] == s2_counts[index]:
                matches += 1
            elif s1_counts[index] == s2_counts[index] + 1:
                matches -= 1

            # make sure the Left is incrementing for each sliding window
            L += 1
        
        return matches == 26


        