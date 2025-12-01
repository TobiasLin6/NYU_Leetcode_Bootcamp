class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        arr = [False] * (target + 1)
        arr[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                arr[j] = arr[j] or arr[j - num]
                
        return arr[target]