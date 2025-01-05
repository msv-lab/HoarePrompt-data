#State of the program right berfore the function call: n is a positive integer and s is a character 'a', 'b', 'c', 'd', 'e', or 'f'.**
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
    #State of the program after the if block has been executed: *n is a positive integer, s is a character 'a', 'b', 'c', 'd', 'e', or 'f', S is the input received from the user, N is an integer derived from S excluding the last character, C is an integer calculated from the last character of S, M is either 1 or 2. If M is in (1, 2), N is updated by adding M, s remains a character 'a', 'b', 'c', 'd', 'e', or 'f', S remains the input received from the user, C remains the same, M is updated to either 2 or 1.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads an input string `S` from the user, extracts an integer `N` from the string excluding the last character, calculates an integer `C` based on the last character of the string, and then performs various arithmetic operations on `N` and `C`. It prints the result of these operations. The function does not accept any parameters and returns no value.

