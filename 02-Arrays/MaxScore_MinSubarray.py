# Maximum Score from Subarray Minimums

class Solution :
    def PairWithMaxSum(self, arr : list[int]) -> int :

        max_sum = float("-inf")

        for i in range(len(arr) - 1) :
            curr_sum = arr[i] + arr[i + 1]
            max_sum = max(max_sum, curr_sum)

        return max_sum
