#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: t is an integer between 0 and 1, k, x, and a are integers from the final input provided.
#Overall this is what the function does:The function processes multiple sets of inputs (t, k, x, a) where t is the number of test cases, and for each test case, it checks if certain conditions are met based on the values of k, x, and a. If the conditions are satisfied, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

