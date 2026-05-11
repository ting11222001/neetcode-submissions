class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        // Output: true

        // across rows
        int top = 0;
        int bottom = matrix.length - 1;

        // within a row
        int left = 0;
        int right = matrix[0].length - 1;

        // find the row
        while (top <= bottom) {
            int mid = (top + bottom) / 2;

            if (matrix[mid][left] > target) {
                bottom = mid - 1;   // go up one row
            } else if (matrix[mid][right] < target) {
                top = mid + 1;      // go down one row
            } else {
                break;  // break out of this loop to start searching within this row
            }
        }

        // recalculate the midRow with the updated top and bottom
        int midRow = (top + bottom) / 2;
        

        // at the current row i.e. mid, search
        while (left <= right) {
            int midCol = (left + right) / 2;

            if (matrix[midRow][midCol] > target) {
                right = midCol - 1;     // go left
            } else if (matrix[midRow][midCol] < target) {
                left = midCol + 1;      // go right
            } else {
                return true;            // found
            }
        }

        return false;
    }
}
