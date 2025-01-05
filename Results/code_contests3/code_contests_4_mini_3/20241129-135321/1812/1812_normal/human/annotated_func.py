#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) representing the row number, and s is a character ('a', 'b', 'c', 'd', 'e', or 'f') representing the seat in that row.
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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `s` is the stripped input from stdin; `S` is the value of `s` after applying the `gets` function; `C` is calculated as ord(S[-1]) - ord('a'); if `M` is either 1 or 2, then `N` is updated to either `N + 1` or `N + 2`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) representing the row number, and a character `s` ('a', 'b', 'c', 'd', 'e', or 'f') representing the seat in that row. It processes the input to calculate a specific value based on the row number and seat position, which is then printed. The function does not handle invalid input cases (such as invalid characters for `s` or non-positive integers for `n`).

