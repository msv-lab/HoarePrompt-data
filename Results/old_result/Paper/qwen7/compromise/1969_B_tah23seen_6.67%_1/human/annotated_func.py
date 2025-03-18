#State of the program right berfore the function call: sChar is a binary string (a string consisting of only '0's and/or '1's) with a length between 2 and 200000.
def func_1(sChar):
    s = []
    for i in sChar:
        s.append(i)
        
    #State: Output State: `sChar` is a non-empty binary string, `i` is the last character in `sChar`, `s` is a list containing every character of `sChar`.
    #
    #In this final output state, the loop has executed for each character in the binary string `sChar`. The variable `s` now contains a list of all characters from `sChar`, in the order they appeared.
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
        
    #State: Output State: `sChar` is a non-empty binary string ending with '0', `i` is the last character in `sChar`, `s` is a list containing every character of `sChar`, `left` is equal to the length of the list `s`, `cost` is 16, `right` is equal to the length of `s`.
    #
    #Explanation: After all the iterations of the loop have finished, the value of `right` will be equal to the length of the list `s`. This is because the loop continues to increment `right` as long as `right` is less than the length of `s` and `s[right]` is not '0'. Once `right` reaches the length of `s` or `s[right]` becomes '0', the condition `right < len(s) and s[right] != '0'` fails, and the loop terminates. The loop also increments `cost` by the value of `right - left + 1` each time it swaps a '0' and '1' and updates `left` and `right` accordingly. Since the loop runs three more times after the initial three iterations, and the cost doubles each time based on the problem's pattern, the final `cost` will be \(2^4 = 16\). The values of `sChar`, `i`, `s`, `left`, and `right` remain unchanged from their final state after the third iteration, where `left` and `right` are both equal to the length of the list `s`.
    return cost
    #The program returns a cost of 16
#Overall this is what the function does:The function accepts a binary string `sChar` and performs a series of swaps to ensure that all '1's are moved to the left side of the string while all '0's are moved to the right side. During this process, it calculates and returns a cost value of 16.

