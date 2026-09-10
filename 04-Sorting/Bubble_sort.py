def bubble_sort(arr) :
    n = len(arr)

    for i in range(n) :
        for j in range(0,n-1-i) :

            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1], arr[j]

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

if arr:
    bubble_sort(arr)
    print(arr)
else:
    print("Array is empty!")
