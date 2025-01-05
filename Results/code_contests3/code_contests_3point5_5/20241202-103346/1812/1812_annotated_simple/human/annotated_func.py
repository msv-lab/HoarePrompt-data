#State of the program right berfore the function call: **The input consists of Vasya's seat in the format ns, where n is a positive integer representing the row number (1 ≤ n ≤ 10^18) and s is a character representing the seat in the row ('a', 'b', 'c', 'd', 'e', 'f').
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
    #State of the program after the if block has been executed: *`S` is the input string obtained from `gets()`, `N` is an integer value derived from `S` after removing the last character and then subtracting either 1 or 2 and adding either 2 or 1, `C` is the ASCII value difference of the last character of `S` and 'a', `M` is either 2 or 1. If M is 1 or 2, the program executes the if part.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads an input string consisting of Vasya's seat in the format ns, where n is a positive integer representing the row number and s is a character representing the seat in the row. It then processes this input to calculate and print a specific result based on the provided constraints. The final output is determined by a series of calculations on the row number, seat character, and predefined formulas. The function does not accept any parameters and operates solely on the provided input.

