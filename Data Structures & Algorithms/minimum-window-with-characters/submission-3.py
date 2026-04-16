class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        res = ""
        freqT = Counter(t)

        def isValid(freq):
            for c in freqT:
                if c not in freq or freqT[c] > freq[c]:
                    return False
            return True
        
        freq = {}
        l, r = 0, 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while isValid(freq):
                res = s[l:r+1] if res=="" or r-l+1 < len(res) else res
                freq[s[l]] -= 1
                l+=1

        return res