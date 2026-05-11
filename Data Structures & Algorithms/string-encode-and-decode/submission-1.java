class Solution {

    public String encode(List<String> strs) {
        // ["neet","code","love","you"] -> "4#neet4#code4#love3#you"
        String res = "";
        for (String s: strs) {
            res += s.length() + "#" + s;
        }
        return res;
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));    // "4#neet4#..." -> j = 0, 1 -> str[0: 1] is from index 0 to 0
            res.add(str.substring(j + 1, j + 1 + length));    // [1 + 1 : 1 + 1 : 4] -> [2: 6] i.e. from index 2 to 5
            i = j + 1 + length; // i = 6 starts next
        }
        return res;
    }
}
