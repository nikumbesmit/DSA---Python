def select(arr, i):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    return min_index

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = select(arr, i)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

if arr:
    selection_sort(arr)
    print(arr)
else:
    print("Array is empty!")
