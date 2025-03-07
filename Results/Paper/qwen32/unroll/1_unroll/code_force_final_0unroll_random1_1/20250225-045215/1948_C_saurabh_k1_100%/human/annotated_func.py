#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an even integer such that 2 ≤ n ≤ 2 \cdot 10^5, and the sum of n over all test cases does not exceed 2 \cdot 10^5. Each of the two strings representing the rows of the grid consists of exactly n characters, each of which is either '<' or '>'. There are no arrows pointing outside the grid.
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
        
    #State: a sequence of "Yes" and "No" responses, one for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two strings of equal even length containing '<' and '>' characters. It determines if it's possible to pair each '<' with a '>' without any crossing arrows and outputs "Yes" if possible, otherwise "No" for each test case.

