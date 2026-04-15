from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        l = 0

        for r in range(len(s2)):
            c[s2[r]] = c.get(s2[r], 0) - 1
            f = True
            
            if r-l+1 > len(s1):
                c[s2[l]] += 1
                l+=1
            
            for ch in c:
                if c[ch] != 0:
                    f = False
                    break

            if f:
                return True
        return False
