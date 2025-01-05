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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `s` is a character ('a', 'b', 'c', 'd', 'e', or 'f'); `S` is the string input after stripping whitespace; if `M` is either 1 or 2, then `N` is either the original value plus 1 or the original value plus 2, and `C` is `ord(S[-1]) - ord('a'); `M` being in (1, 2) indicates that `M` has been toggled between 1 and 2.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (representing the row number) and a character `s` (representing the seat in that row). It processes the input to compute a specific output based on the row number and seat character, which is calculated using the formula involving `N` and `C`. The function does not return any value; it directly prints the computed result. The logic accounts for specific cases based on the row number, but does not handle potential invalid input scenarios or constraints outside the provided expectations.

