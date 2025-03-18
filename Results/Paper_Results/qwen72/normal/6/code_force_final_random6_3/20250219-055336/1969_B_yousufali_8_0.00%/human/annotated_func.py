#State of the program right berfore the function call: The function `func_1` does not take any parameters, but it reads a binary string `s` from the input, where `s` is a list of integers (0s and 1s). The length of `s` is at least 2 and at most 200,000.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: After the loop executes all iterations, `i` is `len(s) - 1`, `n` is the number of 1s in the list `s`, and `ans` is the sum of `n + 1` for each 0 in `s` that is preceded by at least one 1.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each 0 in s that is preceded by at least one 1, and n is the number of 1s in the list s)
#Overall this is what the function does:The function `func_1` reads a binary string `s` from the input, where `s` is a list of integers (0s and 1s) with a length between 2 and 200,000. It processes this list and prints the sum of `n + 1` for each 0 in `s` that is preceded by at least one 1, where `n` is the count of 1s encountered before the 0. The function does not return any value. After the function concludes, the input list `s` remains unchanged, and the final state of the program includes the printed result.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is `t-1`, and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. After the function concludes, `t` is the number of times `func_1` was called, and the final state of the program includes the side effects of `func_1` being called `t` times.

