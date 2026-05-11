class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) space
        # in: [1,2,3,4]
        # out: [24,12,8,6]
        # this solution will have different pref and suff arrays

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1         # [1, 0, 0, 0]
        suff[n - 1] = 1     # [0, 0, 0, 1]

        # create pref
        for i in range(1, n):                       # i: 1, 2, 3
            pref[i] = nums[i - 1] * pref[i - 1]   # [1, 1, 2, 6]

        print(pref)

        # create suff
        for i in range(n - 2, -1, -1):              # i: 2, 1, 0
            suff[i] = nums[i + 1] * suff[i + 1]   # [24, 12, 4, 1]

        # create res
        for i in range(n):
            res[i] = pref[i] * suff[i]              # [24,12,8,6]

        return res