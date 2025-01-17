#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        tents = a
        
        if b % 3 == 0:
            tents += b // 3
        elif b % 3 == 1:
            if c >= 2:
                tents += b // 3 + 1
                c -= 2
            else:
                print(-1)
                continue
        elif b % 3 == 2:
            if c >= 1:
                tents += b // 3 + 1
                c -= 1
            else:
                print(-1)
                continue
        
        if c >= 0:
            tents += c // 3 + (1 if c % 3 > 0 else 0)
            print(tents)
        else:
            print(-1)
        
    #State of the program after the  for loop has been executed: `t` is the number of iterations (a non-negative integer), `a` is the last value of `a` input, `b` is the last value of `b` input, `c` is the last value of `c` input, and `tents` is the sum of the initial value of `a` plus the cumulative increments based on the conditions described. If the loop does not execute at all, `t` is 0, `a`, `b`, and `c` are their original input values, and `tents` is -1 if any condition fails to meet the requirement.
#Overall this is what the function does:The function `func` accepts a positive integer `t` (1 ≤ t ≤ 10^4) and three non-negative integers `a`, `b`, and `c` (0 ≤ a, b, c ≤ 10^9). It processes `t` test cases, where for each test case, it calculates a value `tents` based on the following rules:
1. Initialize `tents` with the value of `a`.
2. Add to `tents` one-third of `b` rounded down if `b` is divisible by 3.
3. If `b` leaves a remainder of 1 when divided by 3 and there are at least 2 universals (`c`), add one-third of `b` rounded down plus 1 to `tents` and reduce `c` by 2. If there are fewer than 2 universals, print `-1` and skip to the next iteration.
4. If `b` leaves a remainder of 2 when divided by 3 and there is at least 1 universal (`c`), add one-third of `b` rounded down plus 1 to `tents` and reduce `c` by 1. If there are no universals, print `-1` and skip to the next iteration.
5. Add to `tents` one-third of `c` rounded down plus 1 if `c` has a remainder when divided by 3. Finally, print the value of `tents` if it is valid, otherwise print `-1`.

After processing all test cases, the function prints `-1` for any test case where the conditions cannot be met. The final state of the program after the function concludes includes:
- `t`: the total number of test cases processed.
- `a`, `b`, and `c`: the last values of the respective input parameters.
- `tents`: the computed value based on the above rules, or `-1` if any condition fails to be met.

