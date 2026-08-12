# These codes find the frequency of a array element

from collections import Counter

raw_input = input("Enter array elements separated by space : ")
arr = [int(x) for x in raw_input.split()]

# Brute force
hashh = [0] * (max(arr) + 1)

for num in arr :
    hashh[num] += 1

# Dictionary
freq_map = {}

for num in arr :
    freq_map[num] = freq_map.get(num,0) + 1

# Using Counter
freq_counter = Counter(arr)

num = int(input("How many elements frequency do u want to check : "))

for i in range(num) :

    element = int(input("Enter your element : "))

    if element:

        target_element = int(element)

        if 0 <= target_element <= max(arr):
            print("\n--- Using Brute force ---")
            print(f"Count of '{target_element}' : {hashh[target_element]}")

        else :
            print("\n--- Using Brute force ---")
            print(f"Count of {target_element} : 0 (Out of hash range)")


        print("\n--- Using Dictionary ---")
        print(f"Count of '{target_element}' : {freq_map.get(target_element,0)}")

        print("\n--- Using Built-in method ---")
        print(f"Counter of '{target_element}' : {freq_counter[target_element]}")

    else:
        print("No element entered.")


