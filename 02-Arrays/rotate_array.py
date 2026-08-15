def rotate_array(arr: list[int], k: int, direction: str = "right") -> list[int]:
    if not arr:
        return []
    
    result = arr[:] 
    n = len(result)
    k = k % n

    def reverse(start: int, end: int) -> None:
        while start < end:
            result[start], result[end] = result[end], result[start]
            start += 1
            end -= 1

    if direction == "right":
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
    else:
        reverse(0, k - 1)
        reverse(k, n - 1)
        reverse(0, n - 1)
    
    return result

raw_input = input("Enter array elements separated by space: ")
arr = [int(x) for x in raw_input.split()]

if not arr:
    print("Array is empty!")
else:
    k = int(input("How many positions do you want to rotate: "))
    
    right_rotated = rotate_array(arr, k, "right")
    left_rotated = rotate_array(arr, k, "left")
    
    print(f"Original Array: {arr}")
    print(f"Right Rotated Array: {right_rotated}")
    print(f"Left Rotated Array: {left_rotated}")   