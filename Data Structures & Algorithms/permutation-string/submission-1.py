from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        s1_sorted = sorted(s1)

        l, r = 0, len(s1)

        while r <= len(s2):
            if s1_sorted == sorted(s2[l:r]):
                return True
            r+=1
            l+=1
        return False