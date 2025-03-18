#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 676, and `t` is now the integer input value; `n` and `k` are integers such that 1 ≤ `n` ≤ 26 and 1 ≤ `k` ≤ 26, but their values are yet to be determined; After the loop executes all iterations, the output consists of `t` lines, each line containing a string generated based on the values of `n` and `k` for each iteration. If `k == 1`, the line will contain `n` repetitions of the character 'a'. Otherwise, the line will contain the string from 'a' to the character corresponding to `k` (inclusive), repeated `(2 - (n == 1))` times.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( t \), \( n \), and \( k \). For each test case, it generates a string based on the values of \( n \) and \( k \). If \( k = 1 \), the string consists of \( n \) repetitions of the character 'a'. Otherwise, the string contains characters from 'a' to the character corresponding to \( k \) (inclusive), repeated \( (2 - (n == 1)) \) times. The function outputs these strings for all test cases.

