#Leetcode - 796. Rotate String

def rotate_string(s : str, goal : str) -> bool :

    if len(s) != len(goal) : return False

    return goal in (s+s)

s = input("Enter your string : ")
goal = input("Enter the string you want to check whether its in \"s\" after roation : ")

print(rotate_string(s,goal))
