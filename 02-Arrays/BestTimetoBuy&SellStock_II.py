# Leetcode - 122. Best Time to Buy and Sell Stock II

class Solution:

  def maxProfit(self, prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
      if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
    return profit


if __name__ == "__main__":
  try:
    user_input = input("Enter stock prices separated by commas: ")
    prices = [int(x.strip()) for x in user_input.split(",")]

    solution = Solution()
    max_profit = solution.maxProfit(prices)

    print(f"Maximum Profit: {max_profit}")

  except ValueError:
    print("Please enter valid integers separated by commas.")
