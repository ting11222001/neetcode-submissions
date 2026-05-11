class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in differences:
                return [differences[difference], i]
            differences[n] = i

        return []



