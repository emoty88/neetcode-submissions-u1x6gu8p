class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        last_seen = nums[0]
        res = 1
        consecutive_count=1
        for i in range(1, len(nums)):
            if last_seen == nums[i]:
                continue
            elif last_seen + 1 ==nums[i]:
                consecutive_count+=1
                last_seen=nums[i]
                res=max(res,consecutive_count)
            else:
                consecutive_count=1
                last_seen=nums[i]
        
        return res