# Count number of Substrings

def SubstrCount(s:str, k:int) -> int :

    if k <= 0 :
        return 0
    
    def atMostK(s:str, k:int) -> int :
        if k < 0 :
            return 0
        
        count = 0
        start = 0
        end = 0
        freq = {}

        for end in range(len(s)) :
            if s[end] not in freq :
                freq[s[end]] = 0
            freq[s[end]] += 1

            while len(freq) > k :
                freq[s[start]] -= 1
                if freq[s[start]] == 0 :
                    del freq[s[start]]
                start += 1
            count += (end - start + 1)

        return count

    return atMostK(s,k) - atMostK(s,k-1)

string = input("Enter your string : ")
k = int(input("Enter no. of distinct character you want in substring : "))

if not string :
    print("String is Empty!...Enter a valid string")
else :
    print(f"Total Substring with {k} distinct character is : {SubstrCount(string,k)}")