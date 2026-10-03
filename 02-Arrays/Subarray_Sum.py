#  Leetcode - 560. Subarray Sum Equals K

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        sum_map = {0: 1}

        for num in nums:
            current_sum += num

            if current_sum - k in sum_map:
                count += sum_map[current_sum - k]
            
            if current_sum in sum_map:
                sum_map[current_sum] += 1
            else:
                sum_map[current_sum] = 1
            
        return count


if __name__ == "__main__":
    
    user_input = input("Enter array elements separated by spaces: ")
    nums = list(map(int, user_input.split()))
    
    k = int(input("Enter target sum (k): "))
    
    sol = Solution()
    ans = sol.subarraySum(nums, k)
    
    print("Number of continuous subarrays with sum k:", ans)
