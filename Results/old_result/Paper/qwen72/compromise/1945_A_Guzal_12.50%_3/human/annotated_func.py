#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The values of `a`, `b`, and `c` are updated based on user input for each iteration of the loop, and `k` is recalculated for each iteration. The final state of `a`, `b`, and `c` will be the values provided in the last iteration of the loop, and `k` will be the value calculated in the last iteration. The value of `n` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, which represents the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the user, representing the number of introverts, extroverts, and universals, respectively. The function calculates a value `k` based on these inputs and prints it. If the conditions `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` are met, it prints `-1`. Otherwise, it calculates `k` as `a + (b + c) // 3` and adds 1 if `(b + c) % 3 != 0`. The function does not return any value, but it prints the result for each test case. After the function concludes, the values of `a`, `b`, and `c` will be the ones from the last test case, and `n` will remain unchanged.

