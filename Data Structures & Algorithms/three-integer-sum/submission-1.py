class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] = -(nums[j] + nums[k])

        # Input: nums = [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
        # Output: [[-1,-1,2],[-1,0,1]]

        nums.sort()  # in-place sorting i.e. modifies the original list in place

        res = set()

        for i in range(0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:      
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    triplet = tuple([nums[i], nums[j], nums[k]])
                    if triplet not in res:
                        res.add(triplet)
                    j += 1
                    k -= 1

        return [list(triplet) for triplet in res]



