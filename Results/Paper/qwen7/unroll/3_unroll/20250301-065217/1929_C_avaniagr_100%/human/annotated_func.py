#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, k is an integer such that 2 ≤ k ≤ 30, x is an integer such that 1 ≤ x ≤ 100, and a is an integer such that 1 ≤ a ≤ 10^9.
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
        
    #State: Output State: The output state consists of 'YES' or 'NO' printed for each iteration of the loop based on the conditions specified in the loop body. The exact sequence of 'YES' and 'NO' depends on the input values provided in each line of the file read by `[*open(0)][1:]`. Each line contains values for `k`, `x`, and `a` which are used to determine the output for that specific iteration.
#Overall this is what the function does:The function reads input from standard input, processes each line containing integers k, x, and a, and prints 'YES' or 'NO' based on specific conditions. For each line, if x is less than k-1, it checks if a is greater than or equal to x+1. If x equals k-1, it checks if a is greater than or equal to x+2. Otherwise, it calculates a value z using a loop and checks if a is greater than or equal to z. The function does not return any value but prints 'YES' or 'NO' for each line of input.

