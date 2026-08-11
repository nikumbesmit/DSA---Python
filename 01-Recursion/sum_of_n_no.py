
def parameterized_sum(n,sum = 0) :
    if n < 1 :
        print(sum)
        return

    parameterized_sum(n-1,sum+n)

def recursive_sum(n) :
    if n == 0 : return 0

    return n + recursive_sum(n-1)

n = int(input("Enter your no : "))

print("\n using parameteres!")
parameterized_sum(n)

print("\n using recursion!")
print(recursive_sum(n))
