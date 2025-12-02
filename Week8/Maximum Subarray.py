class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        g_max = nums[0]
        curr_max = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            curr_max = max(num, curr_max + num)
            
            g_max = max(g_max, curr_max)
            
        return g_max
        