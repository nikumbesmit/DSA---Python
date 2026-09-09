#LeetCode - 451. Sort Characters By Frequency

from collections import Counter

def Sort_char_by_frequency(s : str) -> str :

    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key = lambda x : x[1], reverse = True)
    result = "".join(i*j for i,j in sorted_chars)

    return result
    # return "".join(char * count for char, count in Counter(s).most_common())

string = input("Enter your string : ")
if not string :
    print("String is empty!")
else :
    print(f"Given string in decreasing order of frequency of char is : {Sort_char_by_frequency(string)}")
