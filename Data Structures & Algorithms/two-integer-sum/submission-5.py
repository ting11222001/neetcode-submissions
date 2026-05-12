class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [4,5,6], target = 10
        diff = target - nums[i]
        
        Create a map with key: value like the below.
        diff: index
        when 4, then 6: 0
        when 5, then 5: 1
        when 6, then found a previous number, 4, that has been looking for me
        -> return [0, 2]
        """
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[diff] = i
        return []