# Leetcode - 1781. Sum of Beauty of All Substrings

from collections import Counter

def beautySum(s: str) -> int:
    total_beauty = 0
    for i in range(len(s)) :
        freq = Counter()

        for j in range(i,len(s)) :
            freq[s[j]] += 1

            max_freq = max(freq.values())
            min_freq = min(freq.values())

            if len(freq) > 1 :
                total_beauty += max_freq - min_freq
    
    return total_beauty

string = input("Enter your string : ")
if not string :
    print(f"{0} -> String is empty...")
else :
    print(f"The Sum of beauty of all substrings is : {beautySum(string)}")