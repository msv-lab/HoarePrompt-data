#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from the user, expecting a binary string represented as a list of integers (0s and 1s).
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` is a list of integers (0s and 1s) with the same length as the initial list, `i` is `len(s) - 1`, `n` is the number of 1s in the list `s`, and `ans` is the sum of `n + 1` for each 0 in `s` that follows at least one 1.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each 0 in s that follows at least one 1, and n is the number of 1s in the list s)
#Overall this is what the function does:The function `func_1` reads a binary string from the user, represented as a list of integers (0s and 1s). It then calculates the sum of `n + 1` for each 0 in the list that follows at least one 1, where `n` is the count of 1s encountered so far. Finally, it prints the calculated sum. The function does not return any value.

#State of the program right berfore the function call: None of the variables in the function signature are used, but the function assumes that `input()` will provide a valid integer `t` where 1 ≤ t ≤ 10^4, and that `func_1()` is defined and will handle the processing of each test case.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 1 and 10^4, inclusive, and the function `func_1` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, where 1 ≤ t ≤ 10^4, and calls the function `func_1` exactly `t` times. The function does not return any value. After the function concludes, the integer `t` is still in memory, and `func_1` has been executed `t` times.

