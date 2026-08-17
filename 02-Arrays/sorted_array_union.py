def built_in_union(arr1 : list[int], arr2 : list[int]) -> list[int] :

    if not arr1 and not arr2 : return []

    set1 = set(arr1) if arr1 else set()
    set2 = set(arr2) if arr2 else set()

    union_array = set1.union(set2)

    return sorted(list(union_array))


def approach(arr1 : list[int], arr2 : list[int]) -> list[int] :

    arr1.sort()
    arr2.sort()

    if not arr1 and not arr2 : return []

    if not arr1: return sorted(list(set(arr2)))
    if not arr2: return sorted(list(set(arr1)))

    n = len(arr1)
    m = len(arr2)
    i,j = 0,0

    union_set = []
    last = None

    while i<n and j<m :
        if arr1[i] < arr2[j] :
            if last != arr1[i] :
                union_set.append(arr1[i])
                last = arr1[i]
            i += 1

        elif arr1[i] > arr2[j] :
            if last != arr2[j] :
                union_set.append(arr2[j])
                last = arr2[j]
            j += 1

        else :
            if last != arr1[i] :
                union_set.append(arr1[i])
                last = arr1[i]
            i += 1
            j += 1

    while i<n :
        if last != arr1[i] :
            union_set.append(arr1[i])
            last = arr1[i]
        i += 1      

    while j<m :
        if last != arr2[j] :
            union_set.append(arr2[j])
            last = arr2[j]
        j += 1


    return union_set



raw_input1 = input("Enter first array values separated by space : ")
arr1 = [int(x) for x in raw_input1.split()]

raw_input2 = input("Enter second array values separated by space : ")
arr2 = [int(x) for x in raw_input2.split()]

if not arr1 and not arr2 :
    print("Both Arrays are Empty!")

else :

    print(f"1st Array -> {arr1}")
    print(f"2nd Array -> {arr2}")
    print(f"Union using Built-in methods -> {built_in_union(arr1,arr2)}")
    print(f"Union using best approach -> {approach(arr1,arr2)}")