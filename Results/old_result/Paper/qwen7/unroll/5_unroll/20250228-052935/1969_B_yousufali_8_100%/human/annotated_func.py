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
        
    #State: Output State: `s` is an input binary string, `n` is 0, `ans` is the sum of `n + 1` for every occurrence of '0' in `s` that follows at least one '1'.
    print(ans)
    #This is printed: ans (where ans is the count of '0's in s that follow at least one '1')
#Overall this is what the function does:The function reads a binary string from the user, counts the number of '0's that are immediately followed by at least one '1', and prints the total count. The function does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided where 2 ≤ |s| ≤ 2 ⋅ 10^5 and s_i ∈ {0, 1}.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t remains the same; s remains unchanged.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it calls another function `func_1()` to process a binary string `s` of length between 2 and 200,000 characters containing only '0's and '1's. After processing all test cases, it does not modify the values of `t` or `s`.

