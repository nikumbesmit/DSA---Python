# Leetcode - 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)

        if k == n :
            return total_sum

        ws = n - k
        curr_sum = sum(cardPoints[ : ws])
        min_subarray_sum = curr_sum

        for i in range(ws,n) :
            curr_sum += cardPoints[i] - cardPoints[i - ws]
            min_subarray_sum = min(min_subarray_sum,curr_sum)
        
        return total_sum - min_subarray_sum

if __name__ == "__main__":

    cardPoints = list(map(int, input("Enter card points: ").split()))
    k = int(input("Enter k: "))

    obj = Solution()
    result = obj.maxScore(cardPoints, k)

    print("Maximum points:", result)
