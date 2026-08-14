def Sorted_and_Rotated(arr) :

    if not arr : 
        return None 

    n = len(arr)
    count = 0

    for i in range(n) :

        if arr[i] > arr[(i+1) % n] :
            count += 1

    # if count <= 1 :
    #     return True
    # else :
    #     return False
    return count <= 1

raw_input = input("Enter array element separated by space : ")
arr = [int(x) for x in raw_input.split()]

result = Sorted_and_Rotated(arr)

if result is not None :
    print(f"Array is Sorted nd Rotated : {result}")

else : 
    print("Array is empty!")