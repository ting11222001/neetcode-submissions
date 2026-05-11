class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: nums = [2,20,4,10,3,4,5]
        # Output: 4
        
        numsSet = set(nums) # {2,20,4,10,3,4,5}

        maxLength = 0
        for num in nums:                            # num: 2
            if (num - 1) not in numsSet:            # check if the num is the start of a sequence
                length = 0
                while (num + length) in numsSet:    # num + length: 2 -> 3 -> 4 -> 5
                    length += 1                     # length: 1 -> 2 -> 3 -> 4
                    if length > maxLength:
                        maxLength = length          # maxLength: 1 -> 2 -> 3 -> 4
        
        return maxLength

                    