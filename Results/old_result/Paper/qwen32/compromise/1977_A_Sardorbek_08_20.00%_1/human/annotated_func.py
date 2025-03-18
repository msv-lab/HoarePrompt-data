#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `n` and `m` are integers such that 1 ≤ n, m ≤ 100, and `a` is an input integer. The loop has printed results for each of its `a` iterations based on the conditions provided.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and checks if both `a` and `b` are even to print 'Yes', otherwise it prints 'No'.

