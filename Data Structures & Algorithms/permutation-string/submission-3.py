class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is like a window, its char counts need to be the same in s2 and continuous, the order doesn't matter
        if len(s1) > len(s2):
            return False

        # ord() = "letter to number", and chr() = "number to letter" 
        # ord('a') = 97, ord('z') = 122, the gap = 25
        s1_counts = { chr(c): 0 for c in range(ord('a'), ord('z') + 1)}  
        s2_counts = { chr(c): 0 for c in range(ord('a'), ord('z') + 1)}

        for i in range(len(s1)):  # start updating the counts for "both" maps with the len(s1) as len(s1) is the window size
            s1_counts[s1[i]] += 1
            s2_counts[s2[i]] += 1

        # initial scan
        matches = 0
        for key in s1_counts:   # s1_counts and s2_counts have the same size i.e. 26 and each key is a letter
            if s1_counts[key] == s2_counts[key]:    # if a letter's count, either 0 or >0, then it's a match
                matches += 1
            else:
                matches += 0

        # print("initial scan: ", matches)
        
        # sliding window
        L = 0
        for R in range(len(s1), len(s2)):  # start from len(s1) as the initial counts map stopped right before len(s1) at line 18
            if matches == 26:     # put this here instead of outside for both initial scan and sliding window
                return True
            
            # adding one new char from the Right into the window
            s2_counts[s2[R]] += 1
            if s1_counts[s2[R]] == s2_counts[s2[R]]:
                matches += 1
            # if both were the same, they would have just one count difference
            # and now if s2's count for that letter is too big, s1 needs to add 1 after s2's count added by 1
            # then reduce the match!
            elif s1_counts[s2[R]] + 1 == s2_counts[s2[R]]:
                matches -= 1
            # print("right: ", matches)

            # removing one char from the Left from the window
            s2_counts[s2[L]] -= 1
            if s1_counts[s2[L]] == s2_counts[s2[L]]:
                matches += 1
            elif s1_counts[s2[L]] - 1 == s2_counts[s2[L]]:
                matches -= 1
            # print("left: ", matches)

            # incrementing the Left pointer by 1
            L += 1

        return matches == 26



        