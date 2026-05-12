class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [4,5,6], target = 10

        Create a map with key: value like the below.
        value: index
        when 4, then 4: 0
        when 5, then 5: 1
        when 6, then 6: 2
        """
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[nums[i]] = i
        return []