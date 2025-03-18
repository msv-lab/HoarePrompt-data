#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The loop has executed all its iterations, meaning `i` has been incremented for each iteration up to `q-1`. For each iteration, the values of `a`, `b`, and `c` are integers as provided by the user. Depending on the conditions met (`a < b < c` or `a < b > c`), the loop printed either 'STAIR' or 'PEAK'. If neither condition was met, it printed 'NONE'. After all iterations, the loop would have printed one of these messages for each of the `q` sets of inputs provided. The variable `i` will be equal to `q-1`, and `q` will remain unchanged. The variable `t` from the initial state will still be within the range 1 ≤ t ≤ 1000, as it was not affected by the loop.
#Overall this is what the function does:The function reads multiple sets of three integers (a, b, c) from the user, each set corresponding to a test case. For each set, it checks if a < b < c or a < b > c. If the first condition is met, it prints 'STAIR'; if the second condition is met, it prints 'PEAK'; otherwise, it prints 'NONE'. After processing all sets, the function does not return any value but prints the results for each set.

