def recursive_reversed_array(arr, left=0, right=None) :

    if right is None :
        right = len(arr) - 1

    if left >= right :
        return

    arr[left], arr[right] = arr[right] , arr[left]

    recursive_reversed_array(arr, left+1, right-1)

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

recursive_reversed_array(arr)

print(arr)