#State of the program right berfore the function call: Vasya's seat is described as ns, where n is a positive integer representing the row number (1 ≤ n ≤ 10^18) and s is a character representing the seat in the row ('a', 'b', 'c', 'd', 'e', or 'f').**
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
    #State of the program after the if block has been executed: *Vasya's seat is described as ns, where n is the new row number, s is the seat character; C can be 0, 1, 2, 3, 4, or 5. If M is either 1 or 2, the program does not update Vasya's seat description.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads input to determine Vasya's seat based on the row number and seat character provided. It calculates and prints the final seat position according to the given constraints. If M is either 1 or 2, it modifies the row number accordingly. The function does not accept any parameters.

