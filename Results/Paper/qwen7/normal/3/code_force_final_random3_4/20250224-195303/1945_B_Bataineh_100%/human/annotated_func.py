#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: Output State: After the loop executes all its iterations, `t` will still be an integer such that 1 ≤ `t` ≤ 10^4, and it will hold the final value it was set to during the last iteration of the loop. The variable `i` will be equal to `t - 1`, indicating that the loop has completed all its iterations. The variables `a`, `b`, and `m` will be the values read from the input during the last iteration of the loop. Depending on the conditions met within the last iteration's if-else block, the output will be either 2, 2 + `m` // `b`, 2 + `m` // `a`, or `m` // `a` + `m` // `b` + 2. All other variables and their states will remain unchanged from their initial or previous iteration states.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads three integers `a`, `b`, and `m`. Based on the values of `a`, `b`, and `m`, it calculates and prints one of four possible results: 2, 2 + `m` // `b`, 2 + `m` // `a`, or `m` // `a` + `m` // `b` + 2. After processing all test cases, it outputs the final calculated result for the last test case.

