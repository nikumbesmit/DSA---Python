def move_zero(arr : list[int]) -> list[int] :

    if not arr : return []

    j = 0

    for i in range(len(arr)) :
        if arr[i] != 0 :
            arr[j],arr[i] = arr[i],arr[j] 
            j += 1

    return arr

raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr :
    print("Array is Empty!")

else : 
    print(f"Intial Array : {arr}")
    print(f"Final Array : {move_zero(arr)}")