#State of the program right berfore the function call: sChar is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `s` is a list containing all characters from `sChar`, in the same order they appeared.
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
        
    #State: The list `s` has all '1's moved to the left side and all '0's moved to the right side, with their relative order preserved. The variable `left` points to the position just after the last '1', `right` points to the position just before the first '0', and `cost` is the total number of swaps performed during the process.
    return cost
    #The program returns the total number of swaps (`cost`) performed to move all '1's to the left and all '0's to the right while preserving their relative order.
#Overall this is what the function does:The function accepts a binary string `sChar` and performs swaps to move all '1's to the left side and all '0's to the right side while preserving their relative order within each group. It then returns the total number of swaps performed during this process.

