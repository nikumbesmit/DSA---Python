#Leetcode - 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int:
    current_depth = 0
    max_depth = 0

    for char in s :
        if char == "(" :
            current_depth += 1
            max_depth = max(current_depth,max_depth)
        
        elif char == ")" :
            current_depth -= 1

    return max_depth

string = input("Enter your expression or string : ")

if not string :
    print("Its Empty...Enter a valid input!")
else :
    print(f"Maximun nesting depth of paranthesis is : {maxDepth(string)}")
