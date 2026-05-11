class Solution {
    public boolean isValidSudoku(char[][] board) {
        /*
        e.g. rows: {0: {1, 2, ...}, 1: {4, 5, ...}, ...}
        e.g. grids: {"0,0": {1, 2, 4, 9, 8,}, "0,1": {5, 3}, ...}
        In Java, you cannot directly access a value in a Map using a tuple like (0, 1) as a key in the form of grids[(0,1)].
        Java does not support the tuple syntax natively.
        */
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> grids = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }

                /*
                There was an error:
                The NullPointerException occurs because the get method of a Map returns null if the key does not exist in the map. 
                When you try to call contains on null, it throws the exception.

                Python’s collections.defaultdict can automatically initialize missing keys with default values (like an empty set).

                In Java, Use putIfAbsent to ensure that each Map key (row, column, or grid) has an associated Set<Character> 
                before trying to access it. This avoids null values being returned by get. 
                */
                rows.putIfAbsent(r, new HashSet<>());
                cols.putIfAbsent(c, new HashSet<>());
                String gridKey = String.format("%d,%d", r / 3, c / 3); // e.g. "0,0", "0,1", etc.
                grids.putIfAbsent(gridKey, new HashSet<>());

                if (rows.get(r).contains(board[r][c]) || 
                    cols.get(c).contains(board[r][c]) || 
                    grids.get(gridKey).contains(board[r][c])) {
                    return false;
                }

                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                grids.get(gridKey).add(board[r][c]);
            }
        }

        return true;
    }
}
