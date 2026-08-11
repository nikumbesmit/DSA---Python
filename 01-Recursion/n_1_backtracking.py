def backtracking(n,i=1) :
    if i > n : return

    backtracking(n,i+1)
    return print(i)

n = int(input("Enter your no. : "))
backtracking(n)