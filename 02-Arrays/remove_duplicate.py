def remove_duplicate(arr) :

    if not arr :
        return 0,[]

    k = 1

    arr.sort()

    for i in range(1,len(arr)) :
        if arr[i] != arr[k-1] :
            arr[k] = arr[i]
            k += 1

    return k,arr[:k]


raw_input = input("Enter array element separated by space : ")

if not raw_input.strip() :
    print("Array is empty!") 

else :

    arr = [int(x) for x in raw_input.split()]

    count,unique_elements = remove_duplicate(arr)

    print(f"No. of unique elements after removal of duplicate from sorted array are : {count}")
    print(f"Unique elemenst are : {unique_elements}")

