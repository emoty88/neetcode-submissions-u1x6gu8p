class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        res = 1
        nums = set(nums)
        def get_cons_count(start):
            res = 1
            while start+1 in nums:
                res+=1
                start+=1
            return res
        
        for n in nums:
            if n-1 not in nums:
                res = max(res, get_cons_count(n))
        return res
                
        