def n_times(n,i=1) :

    if i > n : return

    print(i)

    return n_times(n,i+1)

n = int(input("How many no. do u want to print : "))
n_times(n)