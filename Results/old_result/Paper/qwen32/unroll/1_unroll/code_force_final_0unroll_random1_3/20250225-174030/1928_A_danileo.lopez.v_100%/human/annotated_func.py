#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: The output state consists of `t` lines, each being either "Yes" or "No", depending on the values of `a` and `b` for each test case. The variables `t`, `a`, and `b` are not retained after the loop finishes.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints "Yes" if either `a` or `b` can be split into two equal parts such that neither part equals the other integer, otherwise it prints "No". The function outputs `t` lines, each being either "Yes" or "No", depending on the values of `a` and `b` for each test case.

