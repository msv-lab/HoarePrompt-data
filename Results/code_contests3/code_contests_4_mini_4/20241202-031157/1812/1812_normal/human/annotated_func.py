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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `N` is either `n`, `n - 1`, or `n + 1`; `C` is the difference between the ASCII value of the last character of `S` and the ASCII value of 'a'; `M` is either 1 or 2.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) representing a row number and a character `s` ('a', 'b', 'c', 'd', 'e', or 'f') representing a seat in that row. It computes a value based on `n` and `s` using specific calculations involving the ASCII value of `s` and bitwise operations on `n`. The function does not return a value; instead, it prints the computed result directly.

