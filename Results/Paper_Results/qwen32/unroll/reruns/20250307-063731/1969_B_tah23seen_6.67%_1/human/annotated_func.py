#State of the program right berfore the function call: sChar is a list of strings, where each string s consists of only the characters '0' and '1', and the length of each string s satisfies 2 <= len(s) <= 2 * 10^5. Additionally, the total sum of the lengths of all strings in sChar does not exceed 2 * 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: s is a list that contains all the strings from sChar in the same order.
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
        
    #State: - `s`: `['0', '0', '0', '1', '1', '1']` (or any permutation where all '1's are before all '0's)
    #- `left`: 3 (points to the first '1' from the left)
    #- `cost`: 9 (total cost of swaps)
    #- `right`: 6 (points to the end of the list)
    #
    #Output State:
    return cost
    #The program returns 9
#Overall this is what the function does:The function accepts a parameter `sChar`, which is a list of strings where each string consists only of the characters '0' and '1'. It calculates and returns the cost of swapping '0's and '1's to group all '0's to the left of all '1's in the concatenated string formed by `sChar`. The cost is determined by the number of swaps needed, where each swap involves moving a '0' to the left of a '1' and the cost is incremented by the distance between the positions of the '0' and '1' plus one. The function returns the total cost of these swaps.

