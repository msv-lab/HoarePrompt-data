#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed for each iteration of the loop based on the conditions given. The specific sequence of these outputs depends on the values of `b` and `c` entered during each iteration. Since the initial value of `t` does not affect the loop's execution, the output state is determined solely by the loop's conditions and the inputs provided within the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( b \) and \( c \) (where \( 1 \leq b, c \leq 100 \)). For each test case, it prints one of four possible responses: 'YES', 'NO', 'Yes', or 'No'. The decision on which response to print is based on the values of \( b \) and \( c \) according to specified conditions. After processing all test cases, the function concludes without returning any value.

