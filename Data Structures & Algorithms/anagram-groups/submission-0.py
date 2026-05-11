class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s)) # "act" -> ['a', 'c', 't'] -> 'act'
            result[sortedS].append(s) # {'act': ['act', 'cat'], 'opst': ['pots', 'tops', 'stop'], 'aht': ['hat']}
        return list(result.values())