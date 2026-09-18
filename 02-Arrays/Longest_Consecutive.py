# 128. Longest Consecutive Sequence

def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
    
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak




user_input = input("Enter space-separated integers (or press Enter for empty): ").strip()

if user_input:
    nums = list(map(int, user_input.split()))
else:
    nums = []

result = longest_consecutive(nums)
print(f"Length of the longest consecutive sequence: {result}")
