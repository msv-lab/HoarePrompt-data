#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's) and its length is at least 2.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is an input binary string, `n` is equal to the total number of '1's in `s`, `ans` is the sum of each block of '0's plus one, and `i` is the index right after the last character of `s`.
    #
    #To explain this in more detail:
    #- The variable `n` keeps track of the number of '1's encountered so far.
    #- The variable `ans` accumulates the count of each block of '0's plus one. This means if there are two consecutive '0's, it contributes 3 to `ans` (2 '0's plus 1).
    #- The variable `i` is the index of the current character being processed in the string `s`.
    #- After the loop completes, `i` will be equal to the length of `s`, indicating that all characters have been processed.
    #- `n` will be the total count of '1's in the string `s`.
    #- `ans` will be the sum of the lengths of all blocks of '0's plus one for each block.
    print(ans)
    #This is printed: ans (where ans is the sum of the lengths of all blocks of '0's plus one for each block in the binary string s)
#Overall this is what the function does:The function processes a binary string `s` and calculates the sum of the lengths of all blocks of '0's plus one for each block. It then prints this sum. The function does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s (2 ≤ |s| ≤ 2⋅10^5) representing the string that needs to be sorted in non-descending order using cyclic shifts.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t`, which represents the number of test cases, must be greater than 0 for the loop to execute all its iterations. Since the loop runs as long as `t` is greater than 0, and no changes are made to `t` within the loop (based on the given information), `t` needs to stay greater than 0 throughout all iterations.
#Overall this is what the function does:The function processes a number of test cases (`t`). For each test case, it checks if a given binary string (`s`) can be sorted in non-descending order using cyclic shifts and prints whether it is possible for each case. The function does not return any value but outputs the result for each test case.

