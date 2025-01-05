#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and s is a character representing a seat in the row, which can be one of 'a', 'b', 'c', 'd', 'e', or 'f'.
def func():
    gets = lambda r=sys.stdin.readline: r().strip()
    S = gets()
    N = int(S[:-1])
    C = ord(S[-1]) - ord('a')
    M = N - 1 & 3
    if (M in (1, 2)) :
        N -= M
        M ^= 3
        N += M
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18; `s` is a character representing a seat in the row. If `M` is either 1 or 2, then `N` is either `N - 1` or `N - 2`, `C` is the result of `ord(s[-1]) - ord('a')`, and `N` is incremented by `M`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (where \(1 \leq n \leq 10^{18}\)) and a character `s` (which can be one of 'a', 'b', 'c', 'd', 'e', or 'f'). It adjusts the value of `n` based on the computed value of `M`, which is determined by the last character of the input string. It then calculates and prints a specific output based on the final values of `n` and `s`. The function does not handle invalid input cases such as characters outside the specified range or input formats that do not match the expected pattern.

