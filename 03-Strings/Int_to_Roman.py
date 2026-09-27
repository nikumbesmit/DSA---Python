# Leetcode - 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        for val, symbol in val_map:
            if num == 0:
                break
            count, num = divmod(num, val)
            result.append(symbol * count)
            
        return "".join(result)


if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    solution = Solution()
    print("Roman Numeral:", solution.intToRoman(num))
