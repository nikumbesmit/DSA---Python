def fibonacci(n) :

    if n <= 1 : return n

    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the position whose value from fibonacci serires you want : "))
print(fibonacci(num))