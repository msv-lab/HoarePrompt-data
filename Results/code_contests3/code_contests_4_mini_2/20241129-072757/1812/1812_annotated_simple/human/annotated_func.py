#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) representing the row index, and s is a character ('a', 'b', 'c', 'd', 'e', or 'f') representing the seat in row n.
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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); if `M` is either 1 or 2, then `N` is increased by either 1 or 2 depending on the value of `M`. If `M` is not in (1, 2), no changes are made to `N`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) representing the row index and a character `s` ('a', 'b', 'c', 'd', 'e', or 'f') representing the seat in that row. It calculates and prints a value based on the adjusted row index and seat character. Specifically, if the modulo of `n-1` with 4 is 1 or 2, `n` is adjusted, and the final output formula computes a specific result based on the modified `n` and the seat character. Note that the function does not return any value; it only prints the result.

