# Leetcode - 50. Pow(x, n)

def myPow(x: float, n: int) -> float:

    if n == 0 :
        return 1
    
    if n < 0:
        x = 1 / x
        n = -n

    half = myPow(x, n//2)

    if n % 2 == 0 :
        return half * half

    else : 
        return half * half * x


try:
    num = float(input("Enter Your No. : "))
    power = int(input("Enter the power of your no. : "))

    if num == 0 and power <= 0:
        print("Error: 0 raised to a non-positive power is undefined.")
    else:
        res = myPow(num, power)
        print(f"{num}^{power} = {res}")

except ValueError:
    print("Please enter valid numeric inputs!")
