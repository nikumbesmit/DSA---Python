def count(arr : list[int]) -> int :

    if not arr : return 0 

    curr_count, max_count = 0,0

    for num in arr :
        if num == 1 :
            curr_count += 1
            max_count = max(max_count,curr_count)
        else :
            curr_count = 0

    return max_count


raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr:
    print("Array is empty!")
else:
    print(f"The maximum consecutive 1s in the array is -> {count(arr)}")  