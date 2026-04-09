class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:return 1
        l, r = 0, 1
        res = 0
        while r < len(s):
            if s[r] in s[l:r]:
                l+=1
            else:
                res = max(res, r-l+1)
                r+=1
        return res
        