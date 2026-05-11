class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input: numbers = [1,2,3,4], target = 3
        # Output: [1,2]

        l = 0
        r = len(numbers) - 1

        res = []
        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
               break
        res.append(l + 1)
        res.append(r + 1)
        return res
        