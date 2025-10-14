class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counters = {
            0: 0,
            1: 0,
            2: 0
        }

        for num in nums:
            if num in counters:
                counters[num] += 1

        for i in range(len(nums)):
            curr_val = -1
            if counters[0] > 0:
                curr_val = 0
            elif counters[1] > 0:
                curr_val = 1
            elif counters[2] > 0:
                curr_val = 2

            nums[i] = curr_val
            counters[curr_val] -= 1