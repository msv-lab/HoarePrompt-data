#State of the program right berfore the function call: **Precondition**: **n is a positive integer, and s is a character from 'a' to 'f'.**
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
    #State of the program after the if block has been executed: *`n` is a positive integer, `s` is a character from 'a' to 'f', `N` is an integer value derived from `S[:-1]` decreased by either 1 or 2, `C` is a value between 0 and 5, `M` is a value between 0 and 3, `M` is either 1 or 2, and after the execution of the if part, `M` is the result of XOR operation with 3 and `N` is increased by the new value of `M`.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads input from the standard input, processes the input to calculate a value based on specific operations, and then prints the result. It does not accept any parameters. The calculations involve manipulating the input values `N`, `C`, and `M` based on certain conditions, and finally, it computes a result using these values and prints it. The function ensures that `N` is a positive integer, `S` is a character from 'a' to 'f', and performs arithmetic operations to derive a final value for output.

