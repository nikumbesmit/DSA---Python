class Solution:
    def TotalFruits(self, arr):
        basket = {}
        start = 0
        max_fruit = 0

        for end in range(len(arr)):
            basket[arr[end]] = basket.get(arr[end], 0) + 1

            while len(basket) > 2:
                basket[arr[start]] -= 1
                if basket[arr[start]] == 0:
                    del basket[arr[start]]

                start += 1

            max_fruit = max(max_fruit, end - start + 1)

        return max_fruit


if __name__ == "__main__":

    user_input = input("Enter fruit types separated by spaces: ")
    arr = list(map(int, user_input.split()))

    sol = Solution()
    ans = sol.TotalFruits(arr)

    print("Maximum total fruits collected:", ans)
