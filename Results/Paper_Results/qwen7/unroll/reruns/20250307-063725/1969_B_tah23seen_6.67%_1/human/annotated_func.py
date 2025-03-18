#State of the program right berfore the function call: sChar is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `s` is a list containing all characters from `sChar`, and `sChar` remains unchanged.
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
        
    #State: The list `s` has been modified such that all '1's appear before all '0's, with their original relative order preserved. The variable `cost` represents the total number of swaps performed during the process.
    return cost
    #The program returns the total number of swaps (`cost`) performed during the process of rearranging the list `s` such that all '1's appear before all '0's, with their original relative order preserved.
#Overall this is what the function does:The function accepts a binary string `sChar` and returns the total number of swaps required to rearrange the string so that all '1's appear before all '0's while preserving their original relative order. The function first converts the string into a list of characters, then iterates through the list to count the necessary swaps.

