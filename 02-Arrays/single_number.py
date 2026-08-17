def find_no(arr : list[int]) -> int :
    if not arr : return None

    result = 0
    for num in arr :
        result ^= num

    return result

raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr:
    print("Array is empty!")
else:
    print(f"The single no. in the array is  -> {find_no(arr)}")  