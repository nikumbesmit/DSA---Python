# Leetcode - 8. String to Integer (atoi)

def myAtoi(self, s: str) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    def parse_number(idx,curr_num,is_neg) :
        if idx >= len(s) or not s[idx].isdigit() :
            return -curr_num if is_neg else curr_num
        
        curr_num = curr_num * 10 + int(s[idx])

        if not is_neg and curr_num >= INT_MAX :
            return INT_MAX
        
        if is_neg and curr_num >= 2**31 :
            return INT_MIN

        return parse_number(idx+1,curr_num,is_neg)

    i = 0
    n = len(s)

    while i < n and s[i] == " " :
        i += 1
    
    is_negative = False
    if i < n and (s[i] == "-" or s[i] == "+") :
        is_negative = (s[i] == "-")
        i += 1
    
    return parse_number(i,0,is_negative)

    
        
