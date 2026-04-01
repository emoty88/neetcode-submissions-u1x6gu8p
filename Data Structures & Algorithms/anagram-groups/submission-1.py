from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            h = [0] * 26
            for c in s:
                h[ord(c)-ord('a')]+=1
            m[tuple(h)].append(s)

        return list(m.values())