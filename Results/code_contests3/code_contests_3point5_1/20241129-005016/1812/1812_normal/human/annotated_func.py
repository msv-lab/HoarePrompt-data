#State of the program right berfore the function call: The input string consists of a positive integer n (1 ≤ n ≤ 10^18) representing the row number and a character s representing the seat in the row ('a', 'b', 'c', 'd', 'e', 'f').**
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
    #State of the program after the if block has been executed: *`N` is a positive integer, `C` is the result of the subtraction operation, `M` is either 0, 1, 2, or 3. If `M` is either 1 or 2, then `N` is incremented by the value of `M`, `C` remains the same, and `M` becomes the result of the XOR operation with 3.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads a string input consisting of a positive integer `n` representing the row number and a character `s` representing the seat in the row. It then performs calculations based on these inputs to determine a result without returning any value. The calculations involve operations on `N`, `C`, and `M`, and the final result is printed. The function does not have explicit return statements, and the postconditions do not accurately reflect the behavior of the code.

