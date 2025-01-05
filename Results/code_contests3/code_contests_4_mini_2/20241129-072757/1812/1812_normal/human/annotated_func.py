#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) representing the row index, and s is a character ('a', 'b', 'c', 'd', 'e', or 'f') representing the seat in that row.
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
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `s` is a character ('a', 'b', 'c', 'd', 'e', or 'f'), `N` is an integer value derived from the string `S` excluding the last character, `C` is either 0, 1, 2, 3, 4, or 5 depending on the last character of `S`, and `M` is calculated as `N - 1 & 3`. If `M` is in (1, 2), then `M` is updated to either 0 or 1 after the operation `M ^= 3`, and `N` is increased by the new value of `M`, resulting in `N` being updated accordingly.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a string input consisting of a positive integer representing the row index (n) and a character representing the seat (s). It calculates and prints a specific value based on the adjusted row index and seat character, but it does not return any value. The function does not handle any potential input errors or edge cases, such as invalid characters for the seat or inputs that do not match the expected format.

