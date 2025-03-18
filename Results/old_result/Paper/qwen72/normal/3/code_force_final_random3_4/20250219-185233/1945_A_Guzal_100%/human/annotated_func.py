#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: After the loop executes all the iterations, `a`, `b`, and `c` are assigned the final set of values provided by the user during the last iteration, `n` is the input integer, and `i` is `n-1`. If `b % 3 != 0` and `b % 3 + c < 3`, then `k` remains 0. Otherwise, `k` is updated. If `(b + c) % 3 != 0`, `k` is set to `k + a + (b + c) // 3 + 1`. If `(b + c) % 3 == 0`, `k` is set to `k + a + (b + c) // 3`.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the user, representing the number of introverts, extroverts, and universals, respectively. The function then calculates and prints a value `k` for each test case. If `b % 3 != 0` and `b % 3 + c < 3`, it prints `-1`. Otherwise, it calculates `k` as `a + (b + c) // 3` and adds 1 if `(b + c) % 3 != 0`. The function does not return any value; it only prints the results for each test case. After all iterations, the final values of `a`, `b`, and `c` are the ones provided in the last test case, and `i` is `n-1`.

