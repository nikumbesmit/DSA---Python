# Leetcode - 1922. Count Good Numbers

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even_count = (n + 1) // 2
        odd_count = n // 2

        total_good_strings = (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD

        return total_good_strings


if __name__ == "__main__":
    n_input = int(input("Enter length n: "))
    
    sol = Solution()
    result = sol.countGoodNumbers(n_input)
    
    print("Total Good Numbers:", result)
