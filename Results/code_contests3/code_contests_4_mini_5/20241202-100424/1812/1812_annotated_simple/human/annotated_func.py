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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18); `s` is a character ('a', 'b', 'c', 'd', 'e', or 'f'); `S` is the input string read by `gets()` and stripped of whitespace; `N` is a positive integer derived from `S` without its last character; `C` is the integer value derived from the last character of `S` subtracted by the integer value of 'a'; `M` is either 1 or 2. If `M` is in (1, 2), then `N` is increased by `M`, and `M` is updated to the value of 2 or 1 respectively.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function reads an input string consisting of a positive integer `N` (representing a row number) followed by a character `s` (representing a seat, which can be 'a' to 'f'). It then computes and prints a numerical value derived from these inputs based on specific calculations involving `N` and the position of `s`. The function does not return any value; it only prints the result.

