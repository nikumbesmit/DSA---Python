# Leetcode - 20. Valid Parentheses 

class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s :
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else
                stack.append(char)
              
        return not stack

if __name__ == "__main__":
    solution = Solution()
    
    user_string = input("Enter a string of brackets (e.g., {[()}): ")
    
    is_valid = solution.isValid(user_string)
    
    print(f"Input: {user_string}")
    print(f"Is Valid: {is_valid}")
