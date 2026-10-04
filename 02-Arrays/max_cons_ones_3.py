# Leetcode - 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0 
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len


if __name__ == "__main__":

    user_input = input("Enter array elements (0s and 1s) separated by spaces: ")
    nums = list(map(int, user_input.split()))
    
    k = int(input("Enter maximum number of zero flips (k): "))
    
    sol = Solution()
    ans = sol.longestOnes(nums, k)
    
    print("Maximum consecutive ones:", ans)
