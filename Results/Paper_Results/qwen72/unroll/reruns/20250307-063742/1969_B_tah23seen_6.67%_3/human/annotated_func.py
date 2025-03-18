#State of the program right berfore the function call: sChar is a binary string (consisting of only '0's and '1's) with a length of at least 2 and at most 200,000.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: s is a list containing each character of the binary string sChar in the same order as they appear in sChar.
    left = 0
    cost = 0
    right = 1
    while left <= right and right < len(s) and (left < len(s)):
        if s[right] == '0' and s[left] == '1':
            s[right], s[left] = s[left], s[right]
            cost += right - left + 1
        
        while right < len(s) and s[right] != '0':
            right += 1
        
        while left < len(s) and s[left] != '1':
            left += 1
        
    #State: `s` is a list with all '1's moved to the left and all '0's moved to the right, `left` is the index of the first '0' in the list (or equal to `len(s)` if there are no '0's), `right` is the index of the last '1' in the list (or equal to `len(s)` if there are no '1's), and `cost` is the total number of swaps performed.
    return cost
    #The program returns the total number of swaps performed, which is the value of the variable `cost`.
#Overall this is what the function does:The function `func_1` accepts a binary string `sChar` and returns the total number of swaps performed to move all '1's to the left and all '0's to the right within the string. The final state of the program is that the input string is transformed into a list `s` where all '1's are at the beginning and all '0's are at the end, and the variable `cost` holds the total number of swaps required to achieve this transformation.

