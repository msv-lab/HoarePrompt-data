#State of the program right berfore the function call: Vasya's seat is represented as ns, where n is a positive integer representing the row number (1 ≤ n ≤ 10^18) and s is a character representing the seat in the row ('a', 'b', 'c', 'd', 'e', 'f').**
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
    #State of the program after the if block has been executed: *Vasya's seat is represented as `ns`, N is the row number extracted from `s` minus either 2 or 1, C is the ASCII value of the seat character in `s` minus 97, M is either 2 or 1.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function `func` reads a seat number `ns` where `n` is the row number (1 ≤ n ≤ 10^18) and `s` is a character representing the seat in the row ('a', 'b', 'c', 'd', 'e', 'f'). It then calculates and prints Vasya's seat number based on the given constraints.

