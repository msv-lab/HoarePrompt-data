#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
def func():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        y = (n - x * a) // b
        
        if x * a + y * b == n:
            print('YES')
            print(x, y)
            exit()
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a positive integer, `b` is an input integer. After all iterations of the loop, if the program has not exited, then there are no non-negative integers `x` and `y` such that the equation `x * a + y * b == n` holds true.
    print('NO')
#Overall this is what the function does:The function reads three integers, n, a, and b, from input, where 1 ≤ n, a, b ≤ 10,000,000. It attempts to find non-negative integers x and y such that the equation x * a + y * b equals n. If it finds such a pair, it prints 'YES' followed by the values of x and y, and then exits the program. If no such pair exists after iterating through all possible values of x, it prints 'NO'. The function does not return any values or accept parameters, and it adequately handles the case where there are no valid (x, y) combinations by printing 'NO'. It is also important to note that the loop iterates through every possible value of x within the limits set by n and a, ensuring it considers all combinations feasibly, while also confirming that x and y are non-negative.

