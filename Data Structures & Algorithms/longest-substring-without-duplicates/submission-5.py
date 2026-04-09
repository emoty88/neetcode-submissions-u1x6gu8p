class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in m and m[s[r]] >= l:
                l = m[s[r]] + 1
            
            m[s[r]] = r
            r+=1
            res = max(res, r-l)

        return res
        