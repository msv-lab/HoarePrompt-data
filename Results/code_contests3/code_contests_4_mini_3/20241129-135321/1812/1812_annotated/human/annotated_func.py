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
    #State of the program after the if block has been executed: *`N` is an integer derived from `S` without its last character. If `M` is either 1 or 2, then `N` is either `(N - 1)` or `(N - 2)`, and after the operation, `N` can be `N` or `N + 1`, while `M` will be either 2 or 1 accordingly.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 10^18) and a character `s` representing a seat ('a', 'b', 'c', 'd', 'e', or 'f'). It calculates a value based on `n` and `s`, specifically using bitwise operations and arithmetic to derive a final result, which is printed. The function does not return any value; it solely outputs the computed value. The logic may lead to unexpected results for certain values of `s`, particularly if `s` is not one of the expected characters.

