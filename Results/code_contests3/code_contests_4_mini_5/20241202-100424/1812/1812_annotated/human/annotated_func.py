#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) representing the row number, and s is a character ('a' to 'f') representing the seat in that row.
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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `s` is a character ('a' to 'f'), `S` is an input string, and `N` is the integer value of `S` without its last character. If `M` is either 1 or 2, then `N` is increased by `M`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a string input representing a positive integer `n` (1 ≤ n ≤ 10^18) and a character `s` ('a' to 'f') that denotes a seat in that row. It calculates and prints a computed value based on `n` and `s`, which appears to involve some arithmetic operations related to the row and seat position, ultimately resulting in a numerical output that may represent a specific seat or position. However, the function does not return any value; it only prints the result.

