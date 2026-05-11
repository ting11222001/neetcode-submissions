class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i in range(len(nums)): # 0, 1
            difference = target - nums[i] # 10 - 5 = 5, 10 - 5 = 5
            if difference in differences:
                return [differences[difference], i] # [0, 1]
            differences[nums[i]] = i # {5: 0}



