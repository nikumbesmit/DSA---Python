# Leetcode - 53. Maximum Subarray
# Kadane's algorithm

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1 : ] :
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
