# Leetcode - 31. Next Permutation

def next_permutation(nums: list[int]) -> None:
    
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1




user_input = input("Enter space-separated integers: ").strip()

if user_input:
    nums = list(map(int, user_input.split()))
else:
    nums = []

print(f"Original array: {nums}")
next_permutation(nums)
print(f"Next permutation: {nums}")
