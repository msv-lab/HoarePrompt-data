#State of the program right berfore the function call: sChar is a binary string (a string consisting of only 0s and 1s) with a length of 2 to 2 \cdot 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `s` is a list containing each character from the binary string `sChar` in the same order as they appear in `sChar`.
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
        
    #State: `s` is a list with all '1's moved to the right and all '0's moved to the left, `left` is the index of the first '1' in the list (or equal to `len(s)` if there are no '1's), `right` is the index of the first '0' after the last '1' (or equal to `len(s)` if there are no '0's), and `cost` is the total number of swaps made to rearrange the list.
    return cost
    #The program returns the total number of swaps made to rearrange the list `s` so that all '1's are moved to the right and all '0's are moved to the left.
#Overall this is what the function does:The function `func_1` accepts a binary string `sChar` and returns the total number of swaps required to rearrange the string so that all '0's are moved to the left and all '1's are moved to the right. After the function concludes, the input string `sChar` remains unchanged, and the function does not modify any external state. The function effectively calculates the minimum number of swaps needed to achieve the desired rearrangement.

