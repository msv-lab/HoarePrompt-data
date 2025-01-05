#State of the program right berfore the function call: n is a positive integer representing the row number, and s is a character representing Vasya's seat in the row ('a', 'b', 'c', 'd', 'e', 'f').**
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
    #State of the program after the if block has been executed: *n is a positive integer representing the row number, s is a character representing Vasya's seat in the row ('a', 'b', 'c', 'd', 'e', 'f'), N is either N or N - 1, C is calculated as described above, M is 1 if M is either 1 or 2.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads an input string, converts part of it to an integer, calculates a value based on the input, and then prints a result. The function does not explicitly return any value, but it processes the row number and Vasya's seat character to determine a specific output.

