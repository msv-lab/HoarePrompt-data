#State of the program right berfore the function call: The input string consists of a positive integer n (1 ≤ n ≤ 10^18) representing the row number and a lowercase letter s representing the seat in the row ('a', 'b', 'c', 'd', 'e', 'f').**
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
    #State of the program after the if block has been executed: *`M` is the result of `(N - 1) & 3`, where `N` is either 3 or 4. If `M` is in (1, 2), then `M` can be either 1 or 0 and `N` can be either 3 or 4.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads an input string consisting of a positive integer `n` representing the row number and a lowercase letter `s` representing the seat in the row. It then processes these inputs to calculate a value based on certain conditions and prints the result. The function does not explicitly return any value. The calculation involves bitwise operations and arithmetic calculations on `n` and `s`, resulting in a final output printed to the console.

