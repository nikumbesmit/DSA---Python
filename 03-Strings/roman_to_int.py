# LeetCode-13. Roman to Integer

def romanToInt(s: str) -> int:
    roman_to_int = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    total = 0
    prev = 0

    for char in s :
        curr = roman_to_int[char]
        if curr > prev :
            total += curr - (2 * prev)
        else :
            total += curr
        
        prev = curr
    
    return total

Roman_no = input("Enter your Roman No. : ")

if not Roman_no :
    print("Enter a valid input!")
else :
    print(f"Conversion of givrn Roman no. to Integer no. is : {romanToInt(Roman_no)}")
