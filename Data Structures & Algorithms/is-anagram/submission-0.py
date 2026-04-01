from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            m[s[i]] += 1
            m[t[i]] -= 1
        
        for c in m:
            if m[c] != 0:
                return False
        return True