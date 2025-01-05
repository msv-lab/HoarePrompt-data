#State of the program right berfore the function call: Vasya's seat is represented as a string in the format ns, where n is a positive integer (1 ≤ n ≤ 10^18) representing the row number and s is a character from 'a' to 'f' representing the seat in the row.**
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
    #State of the program after the if block has been executed: *Vasya's seat is represented as a string in the format `ns`, where `n` is a positive integer (1 ≤ n ≤ 10^18) representing the row number and `s` is a character from 'a' to 'f'; `N` is the row number of Vasya's seat after executing the code; `C` is the ASCII value of the character `s` in Vasya's seat string minus the ASCII value of 'a'; `M` is calculated as `N - 1 & 3`, and after executing `M ^= 3`, the new value of `M` is calculated. If the new value of `M` is 1 or 2, the overall program state remains the same as the initial state described in the precondition.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads Vasya's seat representation as a string in the format ns, where n is a positive integer (1 ≤ n ≤ 10^18) representing the row number and s is a character from 'a' to 'f' representing the seat in the row. It then calculates a value based on the row number and seat character, but it lacks a return statement. The outcome of the calculation is printed.

