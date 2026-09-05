#Leetcode - 1903. Largest Odd Number in String

def largest_odd_no(num : str) -> str :

    for i in range(len(num) -1 , -1, -1) :

        if int(num[i]) % 2 != 0 :
            return num[ : i+1]

    return ""

num = input("Enter your string of numbers :")

if not num :
    print("String is empty!")
else :
    print(f"Largest odd no. of string is : {largest_odd_no(num)}")
