# Leetcode - 75. Sort Colors


def sortColors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high :
        if nums[mid] == 0 :
            nums[low] , nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1 :
            mid += 1
        
        else :
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

if not arr:
    print("Array is empty!")
else:
    sortColors(arr)
    print(f"Sorted Color array is -> {arr}")  
