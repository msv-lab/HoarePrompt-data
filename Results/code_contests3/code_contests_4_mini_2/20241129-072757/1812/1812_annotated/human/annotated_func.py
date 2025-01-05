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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `s` is a character ('a', 'b', 'c', 'd', 'e', or 'f'), `S` is the string input, `N` is an integer obtained from `S` excluding the last character, and `C` is ord(S[-1]) - ord('a'). If `M` is in (1, 2), then `N` is updated to either N - 1 + 1 or N - 2 + 2 depending on the previous value of `M`, and `M` is changed to either 2 or 1 based on its previous value. Otherwise, no changes are made.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a string input comprising a positive integer representing the row number (1 ≤ n ≤ 10^18) and a character representing the seat (either 'a', 'b', 'c', 'd', 'e', or 'f'). It processes this input to compute and print a value based on the row number and seat character, which includes adjustments to the row number if certain conditions are met. The function does not explicitly return a value but directly prints the computed result.

