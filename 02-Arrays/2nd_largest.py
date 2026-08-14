def Second_largest(arr) :

    if not arr :
        return None

    largest = second_larg = -1 

    for num in arr :

        if num > largest :
            second_larg = largest
            largest = num

        elif num > second_larg and num != largest :
            second_larg = num

    return second_larg

raw_input = input("Enter array element separated by space : ")
arr = [int(x) for x in raw_input.split()]

result = Second_largest(arr)

if result is not None :
    print(f"Secomd Largest element of array is : {result}")

else : 
    print("Array is empty!")