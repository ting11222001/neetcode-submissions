class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Input: piles = [1,4,3,2], h = 9
        // Output: 2
        // 1 <= k <= max(piles)
        // sum(ceil(piles[i] / k)) = current_h and current_h <= h
        // find the optimal k by Binary search

        int leftK = 1;
        int rightK = Arrays.stream(piles).max().orElse(Integer.MIN_VALUE);
        int result = rightK;

        while (leftK <= rightK) {       // k = [1,2,3,4]
            int midK = (leftK + rightK) / 2;
            int curr_h = 0;
            for (int pile: piles) {
                curr_h += Math.ceil((double) pile / midK);  // without double, it will truncate the decimal rather than giving the correct ceiling value
            }

            if (curr_h <= h) {
                rightK = midK - 1;
                result = Math.min(result, midK);
            } else if (curr_h > h) {
                leftK = midK + 1;
            }
        }
        
        return result;
    }
}
