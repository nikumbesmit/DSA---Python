i = 0

def n_name(n,name,i=0) :

    if i == n : return

    print(name)

    return n_name(n,name,i+1)

n = int(input("Enter how many times you want to print your name :"))
name = input("Enter name to be printed : ")

n_name(n,name)