def n_to_1(n) :

    if n < 1 : return

    print(n)

    return n_to_1(n-1)
    
n = int(input("Enter your no. : "))
n_to_1(n)