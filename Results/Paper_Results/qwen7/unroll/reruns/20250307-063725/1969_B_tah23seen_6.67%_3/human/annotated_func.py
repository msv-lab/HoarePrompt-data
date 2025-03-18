#State of the program right berfore the function call: sChar is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `sChar` is a binary string with a length between 2 and 200000; `s` is a list containing all characters of `sChar`.
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
        
    #State: Output State: The string `s` has been rearranged such that all '1's are moved to the left side of the string and all '0's are moved to the right side. The variable `cost` represents the total number of swaps performed during the process, and it is equal to the sum of the lengths of all segments of consecutive '0's found between '1's, plus the positions of these '1's.
    #
    #The `left` and `right` pointers have traversed the string, and they will eventually stop at positions where no more swaps can be made according to the given conditions. The `s` list now contains a sorted version of the original binary string with '1's on the left and '0's on the right, and the `cost` variable holds the total count of such swaps.
    return cost
    #The program returns the total number of swaps (`cost`) performed to rearrange the string `s` such that all '1's are on the left and all '0's are on the right. This `cost` is equal to the sum of the lengths of all segments of consecutive '0's found between '1's, plus the positions of these '1's.
#Overall this is what the function does:The function accepts a binary string `sChar` and returns the total number of swaps (`cost`) needed to rearrange the string so that all '1's are on the left and all '0's are on the right. This `cost` is calculated as the sum of the lengths of all segments of consecutive '0's found between '1's, plus the positions of these '1's.

