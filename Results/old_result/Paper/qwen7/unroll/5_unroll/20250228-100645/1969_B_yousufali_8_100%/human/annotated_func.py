#State of the program right berfore the function call: s is a binary string (consisting only of '0's and '1's), and the length of s is at least 2.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is an input binary string, `n` is 0, `ans` is the sum of `n + 1` for each occurrence of '0' in `s` where `n` is the count of consecutive '1's before the '0'.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each occurrence of '0' in s, with n being the count of consecutive '1's before the '0')
#Overall this is what the function does:The function reads a binary string from the user, counts the number of occurrences of '0' in the string, and for each '0', it adds the count of consecutive '1's before it plus one to a total sum. Finally, it prints the total sum.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s (2 ≤ |s| ≤ 2⋅10^5) representing the string that needs to be sorted in non-descending order using cyclic shifts.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t test cases have been processed, but the specific actions within func_1() are unknown.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it processes a binary string `s` and determines whether `s` can be sorted in non-descending order through cyclic shifts, returning a result for each test case.

