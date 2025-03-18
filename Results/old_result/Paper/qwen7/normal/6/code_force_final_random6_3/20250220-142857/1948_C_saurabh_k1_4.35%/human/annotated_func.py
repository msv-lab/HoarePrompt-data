#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5 and n is even; the input consists of t test cases, each test case includes the width n of the grid (2 ≤ n ≤ 2 \cdot 10^5 and n is even), followed by two strings of length n, where each string consists only of '<' and '>' characters representing the arrows in the first and second rows of the grid respectively.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer reduced to 0 after all iterations, `b` is a list of strings obtained from the last input, `a` is a list of strings obtained from the last input.
#Overall this is what the function does:The function processes up to 10,000 test cases. Each test case involves an even integer \( n \) (2 ≤ n ≤ 2·10^5) representing the width of a grid, followed by two strings of length \( n \) consisting only of '<' and '>' characters representing the arrows in the first and second rows of the grid, respectively. For each test case, the function checks if it's possible to move from any cell in the first row to any cell in the second row following the arrows without violating the movement rules. If such a path exists, the function prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function does not return any value but prints the result for each test case.

