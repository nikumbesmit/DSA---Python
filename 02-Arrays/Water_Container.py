# Leetcode - 11. Container With Most Water

from typing import Optional


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        current_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water



user_input = input("Enter space-separated heights: ").strip()

if user_input:
    height = list(map(int, user_input.split()))
else:
    height = []

result = max_area(height)
print(f"Maximum water container area: {result}")
