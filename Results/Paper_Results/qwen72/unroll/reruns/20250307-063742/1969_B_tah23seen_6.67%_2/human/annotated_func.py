#State of the program right berfore the function call: sChar is a binary string (consisting of only '0' and '1' characters) with a length of at least 2 and at most 2 \cdot 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: s is a list containing the characters of the binary string sChar in the same order.
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
        
    #State: `s` is a list with all '1's moved to the left and all '0's moved to the right, `left` is the index of the first '0' (or the length of the list if there are no '0's), `cost` is the total number of swaps performed, `right` is the index of the first '0' (or the length of the list if there are no '0's).
    return cost
    #The program returns the total number of swaps performed to move all '1's to the left and all '0's to the right in the list `s`.
#Overall this is what the function does:The function `func_1` accepts a binary string `sChar` and returns the total number of swaps needed to move all '1's to the left and all '0's to the right in the string. After the function concludes, the input string `sChar` remains unchanged, and the function does not modify any external state. The function's primary purpose is to compute the cost of rearranging the characters in the string to achieve the desired order.

