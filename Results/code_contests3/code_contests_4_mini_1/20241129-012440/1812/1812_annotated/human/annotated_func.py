#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) representing the row number, and s is a character from 'a' to 'f' representing the seat in that row.
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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `s` is a character from 'a' to 'f', `S` is an input string, `N` is the integer value of `S` excluding the last character, `C` is the integer value of the last character of `S`, and `M` is either 1 or 2. If `M` is 1, then `N` is updated to `N + 1`. If `M` is 2, then `N` is updated to `N + 2`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) representing a row number and a character `s` (from 'a' to 'f') representing a seat in that row. It computes and prints a specific value based on these inputs, calculated using the formula `(N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C)`, where `N` is derived from `n` and `C` is the integer value of the seat character. The exact meaning of this output is not detailed in the provided annotations. The function does not handle invalid inputs or errors, such as non-integer or out-of-range values.

