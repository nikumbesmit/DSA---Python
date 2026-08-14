def largest(arr) :

    if not arr :
        return None

    max = 0

    for num in arr :
        if num > max :
            max = num

    return max 

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

result = largest(arr)

if result is not None :
    print(f"Largest array element : {result}")

else :
    print("Array is empty!")