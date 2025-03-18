#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (2 ≤ n ≤ 2 \cdot 10^5) where n is even, followed by two strings each of length n consisting of '<' and '>' characters representing the arrows in the grid. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: After processing all test cases, the variables `t`, `n`, `a`, and `b` will hold the values from the last test case. The loop control variables (`_` and `i`) will not be accessible outside the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length composed of '<' and '>' characters. For each test case, it determines if there exists a specific pattern of '<' characters that violates a certain condition. If such a pattern is found, it outputs 'No' for that test case; otherwise, it outputs 'Yes'. After processing all test cases, the function concludes without altering the input variables beyond the last test case processed.

