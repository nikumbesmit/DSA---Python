#LeetCode - 205. Isomorphic Strings

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t) : return False

    st = {}
    ts = {}

    for i,j in zip(s,t) :

        if i in st :
            if st[i] != j :
                return False
        else :
            st[i] = j

        if j in ts :
            if ts[j] != i :
                return False
        else :
            ts[j] = i

    return True

s = input("Enter 1st string : ")
t = input("Enter 2nd string : ")

print(f"Are the string isomorphic : {isIsomorphic(s,t)}")
