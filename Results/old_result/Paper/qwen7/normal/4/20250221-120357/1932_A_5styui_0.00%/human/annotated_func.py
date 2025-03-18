#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.') and there will always be at least one valid move from the starting cell.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: The loop has executed all its iterations, `s` is 0, `t` is a positive integer such that \(1 \leq t \leq 1000\), `a` is the total number of iterations the loop executed, `b` is the last input string provided, and `d` is the last input integer provided.
#Overall this is what the function does:The function processes input data for up to 1000 test cases. For each test case, it reads an integer n and a string of length n containing '.', '@', and '*', counts the number of '@' characters (representing coins) in the string, and prints this count. After processing all test cases, the function ends with all relevant variables reset.

