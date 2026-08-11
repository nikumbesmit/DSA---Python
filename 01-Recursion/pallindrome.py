def check_palindrome(name,left=0, right=None) :
    if right is None:
        right = len(name) - 1

    if left >= len(name)/2 :
        return True

    if name[left] != name[right] : return False

    return check_palindrome(name,left+1, right-1)

name = input("Enter word to check : ")
if check_palindrome(name):
    print(f"'{name}' is a palindrome!")
else:
    print(f"'{name}' is NOT a palindrome.")    