# Leetcode - 1.Two Sum (Returns the list of element whose sum is equals to target)

from typing import List

def Two_Sum(arr : List[int],target : int) -> List[int] :

    seen = {}

    for i, num in enumerate(arr) :
        complement = target - num
        if complement in seen :
            return [complement,num]

        seen[num] = i
    return None

raw_values = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

target = int(input("Enter the no. whose sum you want to find :"))

result = Two_Sum(arr,target)

if result:
        print(f"The 2 elements whose sum equals {target} are: {result}")
else:
    print(f"No two elements sum to {target}.")
