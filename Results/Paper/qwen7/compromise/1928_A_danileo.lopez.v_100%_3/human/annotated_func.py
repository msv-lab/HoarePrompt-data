#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: Output State: The output state depends on the inputs provided during each iteration of the loop. For each input pair (a, b), if either a or b is even, and the conditions specified in the if statements are met, "Yes" will be printed; otherwise, "No" will be printed for that iteration. The final output state is a series of "Yes" or "No" based on the given inputs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: `t`, `a`, and `b`. It checks if either `a` or `b` is even. If so, it further checks specific conditions involving division of `a` and `b` by 2. Based on these conditions, it prints 'Yes' or 'No' for each test case. After processing all test cases, it outputs a series of 'Yes' or 'No' values corresponding to the given inputs.

