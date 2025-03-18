#State of the program right berfore the function call: s is a binary string (consisting of only '0's and '1's) and has a length of at least 2.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: The final value of `ans` is the sum of all increments made during the loop, and `n` retains its last value after the loop completes. The variable `i` will be equal to the length of the list `s`.
    print(ans)
    #This is printed: ans (where ans is the sum of all increments made during the loop)
#Overall this is what the function does:The function reads a binary string from the user, counts the number of consecutive '1's, and calculates the sum of all such groups plus one for each group. It then prints the total sum. The function does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided where 2 ≤ |s| ≤ 2 ⋅ 10^5 and s consists only of '0' and '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t must be at least 3.
#Overall this is what the function does:The function processes a specified number of test cases (determined by the integer `t`). For each test case, it calls another function `func_1()` to process a binary string `s`. After processing all test cases, the function ensures that `t` is at least 3.

