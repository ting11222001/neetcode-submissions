class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Input: piles = [1,4,3,2], h = 9
        # Output: 2

        '''
        k is the number of bananas to eat per hour

        Koko can only eat one pile per hour

        find the min speed, k, to eat all the piles

        k can't be 0, so 1 <= k

        Also, len(pile) <= hour

        if k equals to the max pile, it means that Koko can eat that largest pile in one hour,
        and she can certainly eat other piles one hour each,
        and this will gurantee us an h that's always lower than the given hours.

        1 <= k <= max(piles[i])

        so the solution set is like this:
        k = [1, ..., max(piles[i])]

        Brute Force solution will be O(max(p) * n) where p is piles[i], n is len(piles)

        If we want to improve the time complexity, 
        we can try reducing the max(p) to log(max(p)) by Binary Search
        '''

        # Brute force -> Binary search
        '''
        [1,4,3,2], h = 9
        k = [1,2,3,4]

        start 1st round of BS:
        when k = 2:
        1 / 2 = 0.5 -> round up to 1, so the h = 1
        4 / 2 = 2 -> h = 1 + 2
        3 / 2 = 1.5 -> h = 1 + 2 + 1.5
        2 / 2 = 1 -> h = 1 + 2 + 1.5 + 1 = 5.5, and round it up to 6, which is smaller than 9

        save this temp k result: 6
        and then continue

        if the current h is smaller than max h, then go left of mid k, vice versa
        (eat less to increase the possible h, and eat more to decrease the possible h)

        if we found a smaller k than the temp k, then update the temp k

        continue until the BS's right pointer is passing the left pointer,
        then stop, return the final temp k as result
        '''


        # k = [1,2,3,4], piles = [1,4,3,2], h = 9
        # instead of creating a new array for k into k = [1,2,3,4], 
        # initialize the below variables for the possible range of k
        left = 1                # left = 1
        right = max(piles)      # right = 11
        res = right             # res = 11

        while left <= right:            # looping through k
            k = (left + right) // 2     # k = (1 + 11) // 2 = 6
            curr_h = 0                  # the current calculated hour for this round

            for pile in piles:
                curr_h += math.ceil(pile / k)   # curr_h = 1 + 1 + 2 + 2 = 6

            if curr_h <= h:
                res = min(res, k)       # res = min(11, 6) = 6
                right = k - 1           # go left i.e. koko can try eating less
            else:
                left = k + 1            # go right i.e. koko can try eating more

        return res


            

        












