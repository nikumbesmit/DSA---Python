# Leetcode - 1358. Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a' : 0, 'b' : 0, 'c' : 0}
        result = 0

        for right in range(len(s)) :
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0 :
                result += len(s) - right
                count[s[left]] -= 1
                left += 1

        return result

if __name__ == '__main__' :
    
    s = input("Enter string: ")

    obj = Solution()
    result = obj.numberOfSubstrings(s)

    print("Number of valid substrings:", result)
