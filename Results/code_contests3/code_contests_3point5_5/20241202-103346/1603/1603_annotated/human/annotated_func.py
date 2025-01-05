#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 10^3. li and ri are integers for each visitor i such that 1 <= li <= ri <= n.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from input, then prints a string based on the value of `n`. It repeats the string '10' a number of times equal to half of `n`, and if `n` is odd, it appends '1' to the end of the string. The function does not accept any parameters explicitly and operates solely on the input values of `n` and `m`.

