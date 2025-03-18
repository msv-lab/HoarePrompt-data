#State of the program right berfore the function call: sChar is a list of strings where each string s consists of only '0' and '1' characters, and the length of each string s satisfies 2 <= len(s) <= 2 * 10^5. Additionally, the total sum of the lengths of all strings in sChar does not exceed 2 * 10^5.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `sChar` is a list of strings where each string `s` consists of only '0' and '1' characters, and the length of each string `s` satisfies 2 <= len(s) <= 2 * 10^5. The variable `s` is a list that contains all the elements from `sChar`.
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
        
    #State: s is a list of all '0's followed by all '1's, left is the number of '0's, right is len(s), cost is the total number of swaps performed.
    return cost
    #The program returns the total number of swaps performed, which is stored in the variable `cost`.
#Overall this is what the function does:The function takes a list of binary strings (`sChar`) as input and returns the total number of swaps needed to rearrange the characters in each string such that no two adjacent characters are the same.

