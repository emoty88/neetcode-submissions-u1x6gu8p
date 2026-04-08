from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(target, shift):
            m = defaultdict(int)
            res = []
            for i in range(shift, len(nums)):
                if target-nums[i] in m:
                    res.append([nums[m[target-nums[i]]], nums[i]])
                m[nums[i]] = i

            return res
        
        res = set()
        for i in range(len(nums)):
            target = 0-nums[i]
            two_sums = twoSum(target, i+1)
            for ts in two_sums:
                ts.append(nums[i])
                res.add(tuple(sorted(ts)))
        
        return [list(x) for x in res]