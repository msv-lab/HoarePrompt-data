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
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 100\); `a` is an input integer; `i` is equal to `a`; `b` is the first input integer; `c` is the second input integer; `q` is a tuple containing `b` and `c`.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be equal to `a` because the loop runs from `0` to `a-1`, inclusive. Therefore, after `a` iterations, `i` will be `a`. The values of `b` and `c` will be the last pair of integers entered by the user during the last iteration of the loop. The variable `q` will hold this last pair as a tuple. All other variables remain in their initial or updated states as per the loop's execution.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads two integers `b` and `c`. Based on the values of `b` and `c`, it prints one of four possible responses: 'YES', 'NO', 'Yes', or 'No'. After processing all test cases, the function does not return any value.

