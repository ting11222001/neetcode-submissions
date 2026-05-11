class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> first = new HashMap<>();
        for (char character: s.toCharArray()) {
            if (!first.containsKey(character)) {
                first.put(character, 0);
            }
            first.put(character, first.get(character) + 1);
        }

        HashMap<Character, Integer> second = new HashMap<>();
        for (char character: t.toCharArray()) {
            if (!second.containsKey(character)) {
                second.put(character, 0);
            }
            second.put(character, second.get(character) + 1);
        }
        
        return first.equals(second);
    }
}
