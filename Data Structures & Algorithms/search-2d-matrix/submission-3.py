class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        # Output: true

        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bottom = row - 1
        while top <= bottom:
            midRow = (top + bottom) // 2

            if matrix[midRow][0] > target:
                bottom = midRow - 1
            elif matrix[midRow][col - 1] < target:
                top = midRow + 1
            else:
                break

        currRow = (top + bottom) // 2       # in other languages, I need to recomputed the midRow aka the current row
        left = 0
        right = col - 1
        while left <= right:
            midCol = (left + right) // 2

            if matrix[currRow][midCol] < target:
                left = midCol + 1
            elif matrix[currRow][midCol] > target:
                right = midCol - 1
            else:
                return True
        
        return False
