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
        
    #State: Output State: The output state depends on the values of `t`, `k`, `x`, and `a` for each iteration of the loop. For each iteration, if the conditions in the loop body are met, 'YES' is printed; otherwise, 'NO' is printed. The final output state is a sequence of 'YES' and 'NO' based on the evaluations of the conditions for each iteration.
#Overall this is what the function does:The function processes a series of inputs, each consisting of integers \( t \), \( k \), \( x \), and \( a \). For each input, it checks specific conditions involving these integers and prints either 'YES' or 'NO' based on whether those conditions are satisfied. After processing all inputs, it outputs a sequence of 'YES' and 'NO' values corresponding to each input's evaluation.

