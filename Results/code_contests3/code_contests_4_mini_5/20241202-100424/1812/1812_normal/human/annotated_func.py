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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `s` is the value read from input after stripping; `S` is the same value as `s`; if `M` is either 1 or 2, then `N` is updated to be either the previous value of `N` + 1 or the previous value of `N` + 2, and `M` is set to 2 if it was initially 1, or 1 if it was initially 2.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a string input that consists of a positive integer `n` (representing the row number) followed by a character `s` (representing the seat in that row). It processes this input to compute a specific output based on seating arrangements. The function does not handle invalid inputs or return error messages for invalid row numbers, and it directly prints the computed result without returning a value. The output is calculated based on the modified value of `n` and the ordinal position of the character `s`.

