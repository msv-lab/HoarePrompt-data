#State of the program right berfore the function call: n is an integer such that 1 <= n <= 50.
def func_1():
    n = int(input())
    if (n <= 1) :
        print('NO')
        #This is printed: NO
    else :
        print('YES')
        #This is printed: YES
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i = 0
        res = ''
        while n > 0:
            if n >= 2:
                res += letter[i % 26] * 2
                n -= 2
            else:
                res += letter[i % 26]
                n -= 1
            
            i += 1
            
        #State: Output State: The final value of `i` will be `n + 1`, `n` will be 0, `letter` is a string containing 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', and `res` will be a string consisting of the character at index `i % 26` in `letter` repeated `n // 2` times if `n` was initially even, or repeated `(n - 1) // 2` times followed by the same character once if `n` was initially odd.
        #
        #To explain further, the loop continues as long as `n` is greater than 0. Each iteration either subtracts 2 from `n` and appends two of the current character to `res` (if `n` is 2 or more), or subtracts 1 from `n` and appends one character to `res` (if `n` is 1). This process repeats until `n` reaches 0. The variable `i` increments by 1 each time the loop runs. Therefore, after the loop finishes, `i` will be equal to the original value of `n` plus 1, and `res` will be constructed based on how many times the loop appended characters to it, which depends on the initial value of `n`.
        print(res)
        #This is printed: ""
    #State: `n` is an integer between 1 and 50 inclusive, `i` is `n + 1`, `letter` is a string containing 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', and `res` is a string consisting of the character at index `i % 26` in `letter` repeated `(n // 2)` times if `n` was initially even, or repeated `((n - 1) // 2)` times followed by the same character once if `n` was initially odd.
#Overall this is what the function does:The function accepts no parameters and returns a string `res`. If the input `n` is 1 or less, it prints 'NO'. Otherwise, it prints 'YES' and constructs a string `res` by repeating characters from 'A' to 'Z' based on the value of `n`. Specifically, if `n` is even, it repeats each character twice; if `n` is odd, it repeats each character twice except for the last character which is repeated once. After constructing `res`, it prints the string.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all the iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that change the value of `t`.
#Overall this is what the function does:The function accepts no parameters and returns nothing. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it calls the `func_1()` function. After processing all test cases, the value of `t` must remain greater than 0.

