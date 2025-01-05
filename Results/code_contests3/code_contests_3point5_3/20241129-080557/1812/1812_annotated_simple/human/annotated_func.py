#State of the program right berfore the function call: The input string consists of a positive integer n (1 ≤ n ≤ 10^18) representing the row number and a character s representing the seat in the row, where s is one of the characters 'a', 'b', 'c', 'd', 'e', 'f'.**
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
    #State of the program after the if block has been executed: *`S` is the input string consisting of a positive integer `n` and character `s`. If `M` is either 1 or 2, `N` is the positive integer extracted from `S` decreased by either 1 or 2 based on the original value of `M` and increased by the new value of `M`. `C` is the result of the calculation `ord(s) - ord('a')`. `M` is either 1 or 8.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function does not accept any parameters. It reads an input string consisting of a positive integer `n` and a character `s` representing the row number and seat in the row respectively. It then calculates the seat position based on the row number and seat character and prints the result. The calculation involves adjusting the row number `N`, seat character `C`, and a value `M` based on certain conditions.

