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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `C` is the ASCII difference between the last character of `S` and 'a'; if `M` is either 1 or 2, then `N` is either `n` (if M is 1) or `n - 1` (if M is 2) after increasing `N` by `M`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (representing the row number, where 1 ≤ n ≤ 10^18) and a character `s` (representing the seat in that row, which must be one of 'a', 'b', 'c', 'd', 'e', or 'f'). It computes a value based on the row number and seat character, specifically adjusting the row number based on certain conditions related to `M`, and then prints a calculated expression involving `N` and the seat character. The function does not return any value, only prints the result.

