#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `n`. At this point, `n` is a non-negative integer, and `a` and `b` are integers from the last input provided within the loop. The final state of `a` and `b` will depend on the conditions checked in the loop:
    #
    #- If both `a` and `b` are odd integers, the loop will print 'NO' for each iteration where this condition holds true.
    #- If the condition `(a / 2 == b and b % 2 != 0) or (b / 2 == a and a % 2 != 0)` is met for any iteration, the loop will print 'NO' and will not proceed further with the current pair of `a` and `b`.
    #- If none of the above conditions are met for any iteration, the loop will print 'YES' for the last valid pair of `a` and `b`.
    #
    #Thus, the final output state is characterized by `i` being equal to `n`, and the values of `a` and `b` reflecting the last input pair processed by the loop, with the last printed statement being either 'YES' or 'NO' based on the conditions evaluated throughout the loop's iterations.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it takes two positive integers \(a\) and \(b\) as input and prints 'YES' if neither \(a\) nor \(b\) are both odd and do not satisfy the specific divisibility conditions, otherwise it prints 'NO'. After processing all test cases, the function outputs the final result for the last tested pair of \(a\) and \(b\).

