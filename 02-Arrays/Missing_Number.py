def find_no(arr : list[int]) -> int :

    n = len(arr)
        
    Expected_sum = (n * (n + 1)) // 2
    Actual_sum = sum(arr)

    return Expected_sum - Actual_sum

print("Array should start from 0 and in sorted order till nth no.!")
raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr:
    print("Array is empty!")
else:
    print(f"The missing no. in the array is -> {find_no(arr)}")  