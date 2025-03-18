#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six positive integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for _ in range(t):
        r, w, a, b, c, d = list(map(int, input().split()))
        
        if a > c:
            print('Draw')
        else:
            x = abs(a - c) // 2
            if abs(a - c) % 2:
                l = max(1, d - x)
                r = min(w, d + x)
                print(*(['Draw'], ['Alice'])[abs(l - b) <= x + 1 and abs(r - b) <= 
                    x + 1])
            else:
                l = max(1, b - x)
                r = min(w, b + x)
                print(*(['Draw'], ['Bob'])[abs(l - d) <= x and abs(r - d) <= x])
        
    #State: After executing the loop for `t` iterations, the output will consist of 'Draw' or either 'Alice' or 'Bob' printed based on the conditions specified in the loop body. The exact sequence of outputs depends on the input values provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of six integers (h, w, x_a, y_a, x_b, y_b). For each test case, it compares the positions x_a and x_b. If x_a is greater than x_b, it prints 'Draw'. Otherwise, it calculates a range based on the difference between x_a and x_b and checks if the position b (or d) falls within this range. Depending on the result, it prints either 'Draw', 'Alice', or 'Bob'. The function does not return any value but prints the results for each test case.

