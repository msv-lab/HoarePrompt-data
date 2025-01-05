#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and s is a character representing a seat, which can be one of 'a', 'b', 'c', 'd', 'e', or 'f'.
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
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18; `s` is a character representing a seat; if `M` is either 1 or 2, then `N` is updated to either `N + 1` or `N + 2`, and `C` remains the integer value of the difference between the ASCII values of the last character of `s` and 'a'.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 10^18) and a character `s` representing a seat ('a', 'b', 'c', 'd', 'e', or 'f'). It calculates a specific value based on the input `n` and the position of `s` in the alphabet, adjusting `n` if needed, and prints the computed result. The function does not return any value; it only prints the result.

