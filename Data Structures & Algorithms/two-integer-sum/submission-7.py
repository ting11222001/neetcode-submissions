class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [4,5,6], target = 10

        Try using enumerate()

        Have to check first in the hashmap, then store.
        This prevents matching a number with itself.

        It's usually called the "hash map lookup" pattern:
        you store values you've already seen in a hash map, 
        then check if the complement exists in O(1).

        value: index
        4: 0
        5: 1
        6: 2
        """
        seen = {} # value: index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []