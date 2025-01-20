#State of the program right berfore the function call: n is an even integer where 2 ≤ n ≤ 100,000, and a is an integer where 1 ≤ a ≤ n.
def func():
    n, a = map(int, input().split())
    if (a <= n // 2) :
        print(a // 2 + a % 2)
    else :
        print((n - a + 1) // 2 + (n - a + 1) % 2)
    #State of the program after the if-else block has been executed: *`n` is an even integer input by the user where 2 ≤ n ≤ 100,000, and `a` is an integer input by the user where 1 ≤ a ≤ n. If `a` ≤ `n // 2`, the value `a // 2 + a % 2` is printed. If `a` > `n // 2`, the result of the expression is printed as a positive integer.
#Overall this is what the function does:The function reads two integers, `n` and `a`, from user input, where `n` is an even integer in the range [2, 100,000] and `a` is an integer in the range [1, n]. It then prints a calculated value based on the following conditions: if `a` is less than or equal to `n // 2`, it prints `a // 2 + a % 2`; otherwise, it prints `(n - a + 1) // 2 + (n - a + 1) % 2`. The function does not return any value. After the function concludes, the state of the program includes the printed value, which is a positive integer representing the result of the specified calculation.

