#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: Output State: The output state consists of a series of 'YES' and 'NO' printed for each iteration of the loop based on the conditions specified in the loop body. For each input line `s`, the values of `k`, `x`, and `a` are read, and depending on these values, either 'YES' or 'NO' is printed. The exact sequence of 'YES' and 'NO' will vary based on the specific values of `k`, `x`, and `a` provided in each iteration.
#Overall this is what the function does:The function reads input from standard input, processes each line containing integers k, x, and a, and prints 'YES' or 'NO' based on specific conditions. After processing all lines, the function concludes without returning any value.

