# Leetcode - 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                res[p2] = total % 10
                res[p1] += total // 10
                
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")


if __name__ == "__main__":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    solution = Solution()
    print("Product:", solution.multiply(num1, num2))
