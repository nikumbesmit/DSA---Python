#LeetCode - 14. Longest Common Prefix
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs :
        return ""

    strs.sort()

    ans = ""
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first),len(last))) :
        if first[i] != last[i] :
            return ans
        
        ans += first[i]

    return ans

words = input("Enter strings separated by space: ").split()
print(f"The Largest common prefix is : {longestCommonPrefix(words)}")
