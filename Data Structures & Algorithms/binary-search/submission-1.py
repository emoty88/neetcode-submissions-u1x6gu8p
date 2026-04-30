class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        m = r//2

        while l<r:

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m
            m_t = l + (r-l)//2
            if m_t == m:
                return -1
            m = m_t


        return -1