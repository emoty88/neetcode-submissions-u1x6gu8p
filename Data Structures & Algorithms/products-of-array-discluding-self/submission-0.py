class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_p = [0] * n
        post_p = [0] * n

        pre_p[0] = nums[0]
        post_p[n-1] = nums[n-1]
        res = []
        for i in range(1,n):
            pre_p[i]=pre_p[i-1]*nums[i]
        
        for i in range(n-2,0,-1):
            post_p[i]=post_p[i+1]*nums[i]
        
        for i in range(n):
            pre_product = pre_p[i-1] if i>0 else 1
            post_product = post_p[i+1] if i<n-1 else 1
            res.append(pre_product * post_product)
        return res


        
        