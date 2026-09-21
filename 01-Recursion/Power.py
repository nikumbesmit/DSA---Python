# Leetcode - 50. Pow(x, n)

def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    product = x

    while n > 0:
        if n % 2 == 1:
            result *= product
        product *= product
        n //= 2

    return result


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
