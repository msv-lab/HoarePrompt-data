#State of the program right berfore the function call: sChar is a binary string (consisting of '0' and '1') with a length of at least 2 and at most 2 * 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `sChar` is a binary string with a length of at least 2 and at most 2 * 10^5, `s` is a list containing all the characters of `sChar` in the same order as they appear in `sChar`.
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
        
    #State: After all iterations of the loop, `sChar` remains a binary string with a length of at least 2 and at most \(2 \times 10^5\), `s` still contains all the characters of `sChar` in the same order, but with all '1's moved to the front and all '0's moved to the back, `left` is equal to the number of '1's in `s`, `right` is equal to `len(s)`, and `cost` is the total sum of `right - left + 1` for each iteration until the loop condition is no longer met.
    return cost
    #The program returns the total sum of `right - left + 1` for each iteration until the loop condition is no longer met, where `left` is the number of '1's in the string `s`, and `right` is the length of the string `s`.
#Overall this is what the function does:The function `func_1` takes a binary string `sChar` as input and returns an integer representing the total cost of rearranging the string such that all '1's are moved to the front and all '0's are moved to the back. The cost is calculated as the sum of `(right - left + 1)` for each swap operation performed during the rearrangement process. After the function executes, the input string `sChar` remains unchanged, but internally, the function creates a list `s` that initially contains the characters of `sChar` in the same order. By the end of the function, `s` will have all '1's at the beginning and all '0's at the end, and the variable `left` will hold the number of '1's in the string.

