def backtracking(n) :
    if n < 1 : return

    backtracking(n-1)
    return print(n)

n = int(input("Enter your no. : "))
backtracking(n)