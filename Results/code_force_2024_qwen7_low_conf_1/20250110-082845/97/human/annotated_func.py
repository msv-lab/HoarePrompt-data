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
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer with \(1 \leq t \leq 10^4\), `tents` is the final value calculated after executing the loop for each of the `t` inputs. For each input:
    #- `a`, `b`, and `c` are integers derived from the input such that `a` is the initial value of `tents`, `b` is the second value, and `c` is the third value.
    #- If `c` is non-negative, `tents` is updated based on the conditions involving `b % 3` and `c`:
    #  - If `b % 3 == 0`, `tents` is incremented by `b // 3`.
    #  - If `b % 3 == 1` and `c >= 2`, `tents` is incremented by `b // 3 + 1` and `c` is decremented by 2.
    #  - If `b % 3 == 2` and `c >= 1`, `tents` is incremented by `b // 3 + 1` and `c` is decremented by 1.
    #- If `c` becomes negative, the loop prints `-1` and stops further updates to `tents`.
    #- If `c` is non-negative at the end of all iterations, `tents` is printed after all the updates.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three non-negative integers `a`, `b`, and `c`. It calculates the maximum number of tents (`tents`) that can be allocated based on certain conditions involving `a`, `b`, and `c`. Specifically, `a` represents the number of introverts, `b` the number of extroverts, and `c` the number of universals (which can be used as either introverts or extroverts). The function updates `tents` according to the following rules:

1. Initialize `tents` with the value of `a`.
2. If `b % 3 == 0`, add `b // 3` to `tents`.
3. If `b % 3 == 1` and `c >= 2`, add `b // 3 + 1` to `tents` and decrement `c` by 2.
4. If `b % 3 == 2` and `c >= 1`, add `b // 3 + 1` to `tents` and decrement `c` by 1.
5. After updating based on `b`, if `c` is non-negative, add up to one more tent (`c // 3 + (1 if c % 3 > 0 else 0)`).

If at any point `c` becomes negative due to the above operations, the function prints `-1` and does not proceed with further updates. Otherwise, it prints the final value of `tents`.

The function accepts `t` test cases and returns no explicit output, but prints the result for each test case during its execution.

