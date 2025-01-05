#State of the program right berfore the function call: n is a positive integer representing the row number, and s is a character representing the seat in that row ('a', 'b', 'c', 'd', 'e', 'f').**
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
    #State of the program after the if block has been executed: *n is a positive integer representing the row number, s is a character representing the seat in that row ('a', 'b', 'c', 'd', 'e', 'f'), C is the result of subtracting the ASCII value of 'a' from the ASCII value of the last character of s, N is the updated row number after subtracting M, where M is either 1 or 2. If M is either 1 or 2, the row number N is updated accordingly.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads input values for row number and seat character, processes them to calculate the seat number, and prints the result. It performs various computations based on the input values to determine the final seat number. The function does not accept any parameters explicitly.

