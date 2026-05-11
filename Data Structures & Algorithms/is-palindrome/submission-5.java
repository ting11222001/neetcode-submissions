class Solution {
    public boolean isPalindrome(String s) {
        String lowercase_s = s.toLowerCase();

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while ((left < right) && !Character.isLetterOrDigit(lowercase_s.charAt(left))) {
                left++;
            }
            while ((right > left) && !Character.isLetterOrDigit(lowercase_s.charAt(right))) {
                right--;
            }
            if (lowercase_s.charAt(left) != lowercase_s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
