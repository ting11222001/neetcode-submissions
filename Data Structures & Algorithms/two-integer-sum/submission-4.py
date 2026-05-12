class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [4,5,6], target = 10
        diff: target - nums[i]
        6: 0
        5: 1
        -> 0, 2
        """
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[diff] = i
        return []