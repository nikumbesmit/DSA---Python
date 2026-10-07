# Leetcode - 930. Binary Subarrays With Sum

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(goal: int) -> int:
            if goal < 0:
                return 0
            
            left = 0
            curr_sum = 0
            count = 0

            for right in range(len(nums)):
                curr_sum += nums[right]

                while curr_sum > goal:
                    curr_sum -= nums[left]
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMost(goal) - atMost(goal - 1)


if __name__ == "__main__":
    user_input = input("Enter binary array elements (0s and 1s) separated by spaces: ")
    nums = list(map(int, user_input.split()))
    
    goal = int(input("Enter target goal sum: "))
    
    sol = Solution()
    ans = sol.numSubarraysWithSum(nums, goal)
    
    print("Number of binary subarrays with sum equal to goal:", ans)
