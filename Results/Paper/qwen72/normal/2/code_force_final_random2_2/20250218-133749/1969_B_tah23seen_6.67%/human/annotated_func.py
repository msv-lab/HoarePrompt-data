#State of the program right berfore the function call: sChar is a binary string (consisting of only '0' and '1') with a length of at least 2 and at most 2 * 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `sChar` is a binary string with a length of at least 2 and at most 2 * 10^5, `s` is a list containing all the characters of `sChar` in the same order, `i` is the last character of `sChar`.
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
        
    #State: After the loop executes all the iterations, `sChar` remains a binary string with a length of at least 2 and at most \(2 \times 10^5\), `s` is a list containing all the characters of `sChar` in the same order but with all '0's moved to the front and all '1's moved to the back, `cost` is the total number of swaps performed to achieve this arrangement, `i` is the last character of `sChar`, `left` is the index of the first '1' in the final `s` (or the length of `s` if no '1' is found), and `right` is the length of `s`.
    return cost
    #The program returns the total number of swaps (`cost`) performed to move all '0's to the front and all '1's to the back in the list `s`.
#Overall this is what the function does:The function `func_1` accepts a binary string `sChar` and returns the total number of swaps required to rearrange the string such that all '0's are moved to the front and all '1's are moved to the back. The original string `sChar` remains unchanged, and the function internally works with a list `s` that contains the characters of `sChar`. After the function concludes, the list `s` will have all '0's at the beginning and all '1's at the end, and the return value is the total number of swaps performed to achieve this arrangement.

