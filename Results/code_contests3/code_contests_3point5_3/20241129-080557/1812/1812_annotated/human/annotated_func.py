#State of the program right berfore the function call: **Precondition**: **n is a positive integer and s is a character from 'a' to 'f'.**
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
    #State of the program after the if block has been executed: *n is a positive integer, s is a character from 'a' to 'f', C is the result of the ASCII subtraction operation, M is a value between 0 and 3. If M is either 1 or 2, M is the result of XOR operation between the current value of M and 3. N is decreased by either 1 or 2 and increased by M.
    print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))
#Overall this is what the function does:The function reads an input string S which consists of a positive integer followed by a character from 'a' to 'f'. It then performs various mathematical operations based on the input values N and C. If M is either 1 or 2, it modifies N and M accordingly. Finally, the function calculates an expression based on the modified N, C, and M, and prints the result.

