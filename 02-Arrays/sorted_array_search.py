def search(arr: list[int], k: int) -> bool:
    if not arr:
        return False

    arr.sort()  
    n = len(arr)

    start = 0         
    end = n - 1

    while start <= end:
       
        mid = (start + end) // 2  

        if arr[mid] == k:
            return True   
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return False

raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr:
    print("Array is empty!")
else:
    k = int(input("Enter the number to search: "))
    result = search(arr, k)

    if result:
        print(f"Element {k} found in the array!")
    else:
        print(f"Element {k} not found in the array.")   