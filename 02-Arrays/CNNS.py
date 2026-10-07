# Leetcode - 1248. Count Number of Nice Subarrays

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k: int) -> int:
            left = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1

                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMost(k) - atMost(k - 1)


if __name__ == "__main__":

    user_input = input("Enter array elements separated by spaces: ")
    nums = list(map(int, user_input.split()))
    
    k = int(input("Enter target number of odd integers (k): "))
    
    sol = Solution()
    ans = sol.numberOfSubarrays(nums, k)
    
    print("Number of nice subarrays:", ans)
