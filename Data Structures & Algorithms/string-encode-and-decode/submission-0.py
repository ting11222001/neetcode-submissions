class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet", "code"] -> "neetcode", and it's possible to have any special characters in a sub-string
        # ["neet","code","love","you"] -> "4#neet4#code4#love3#you"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":  # e.g. "4#..." stops at j = 1
                j += 1
            length = int(s[i:j])  # [i:j] will be 0, excluding 1 -> s[i:j] = "4" -> length: 4
            res.append(s[j + 1: j + 1 + length])  # append from behind "#" -> e.g. 4#neet, which starts j = 2, i.e. from "n"
            i = j + 1 + length  # i: 1 + 1 + 4 = 6
        return res
