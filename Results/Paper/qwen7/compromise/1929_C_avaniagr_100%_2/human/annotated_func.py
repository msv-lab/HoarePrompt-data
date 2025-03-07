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
        
    #State: Output State: The loop processes each line of input until there are no more lines to process. For each line, the values of `k`, `x`, and `a` are read and used to determine whether to print 'YES' or 'NO'. If `x < k - 1` and `a >= x + 1`, it prints 'YES' and checks if `a` remains greater than or equal to `x + 1`. If `x == k - 1` and `a >= x + 2`, it prints 'YES' and does not change `a`. If `x > k - 1`, it calculates `z` as described in the loop and checks if `a >= z` before printing 'YES' or 'NO'. After processing all lines, the final state of `[*open(0)]` will be a list containing the remaining lines of input that were not processed, and the values of `k`, `x`, and `a` will reflect the last set of values read from the input.
    #
    #In summary, the output state after the loop executes all iterations will be a list `[*open(0)]` containing any remaining unprocessed lines of input, and the values of `k`, `x`, and `a` will be the last values read from the input.
#Overall this is what the function does:The function reads multiple lines of input, each containing three integers \( k \), \( x \), and \( a \). Based on the values of \( k \), \( x \), and \( a \), it prints either 'YES' or 'NO'. After processing all input lines, it leaves the remaining unprocessed lines in the input buffer and updates \( k \), \( x \), and \( a \) to their last read values. The function does not return any value.

