#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers a and b such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: For each of the `t` test cases, the program will print either 'Yes' or 'No' based on the conditions specified in the loop. The variables `a` and `b` will be re-assigned for each iteration, but `t` will remain unchanged. The state of `t` and any other variables not involved in the loop body will remain the same as the initial state.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'Yes' if either `a` or `b` can be split into two equal parts such that neither part is equal to the other integer, and 'No' otherwise.

