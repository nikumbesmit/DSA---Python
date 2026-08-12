# These codes find the frequency of a character from the String

from collections import Counter


raw_string = input("Enter your string : ")

# Using Brute force
hashh = [0] * 256

for char in raw_string :
    hashh[ord(char)] += 1

# Using Dictionary
freq_map = {}

for char in raw_string :
    freq_map[char] = freq_map.get(char,0) + 1

# Using built-in method
freq_counter = Counter(raw_string)

num = int(input("How many characters frequency do u want to check : "))

for i in range(num) :

    char_input = input("Enter your character : ")

    if char_input:

        target_char = char_input[0]

        print("\n--- Using Brute force ---")
        print(f"Count of '{target_char}' : {hashh[ord(target_char)]}")

        print("\n--- Using Dictionary ---")
        print(f"Count of '{target_char}' : {freq_map.get(target_char,0)}")

        print("\n--- Using Built-in method ---")
        print(f"Counter of '{target_char}' : {freq_counter[target_char]}")

    else:
        print("No character entered.")