class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,3,4] -> out: [24,12,8,6]
        # pre: [1,1,2,6]
        # suf: [24,12,4,1]
        # res: [24,12,8,6]
        pre = 1
        post = 1
        res = []

        for num in nums:
            res.append(pre)
            pre = pre * num
        
        for i in range(len(nums) - 1, -1, -1): # sop before reaching -1, and decrement by 1 at each step
            res[i] *= post
            post *= nums[i]

        return res

        
       