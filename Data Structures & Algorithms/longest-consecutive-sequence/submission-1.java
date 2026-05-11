class Solution {
    public int longestConsecutive(int[] nums) {
        // Input: nums = [2,20,4,10,3,4,5]
        // Output: 4

        Set<Integer> numsSet = new HashSet<>();

        for (int num: nums) {
            numsSet.add(num);                               // numsSet: [2,20,4,10,3,4,5]
        }

        int maxLength = 0;
        for (int num: nums) {                               // 2 -> 20 -> 4 -> 10 -> 3 -> 4 -> 5
            if (!numsSet.contains(num - 1)) {
                int length = 0;
                while (numsSet.contains(num + length)) {    // 2 -> 3 -> 4 -> 5; 20; 10
                    length++;                               // 1 -> 2 -> 3 -> 4; 1; 1
                    if (length > maxLength) {
                        maxLength = length;                 // 1 -> 2 -> 3 -> 4
                    }
                }
            }
        }

        return maxLength;
    }
}
