#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'Draw', 'Alice', or 'Bob', depending on the input values for each iteration of the loop. For each iteration, if `a > c`, it prints 'Draw'. Otherwise, it calculates `x` as half the absolute difference between `a` and `c`. If the absolute difference is odd, it sets `l` and `r` based on `d` and checks if `b` falls within the range `[l, r]` with a tolerance of `x+1`. If so, it prints 'Alice'; otherwise, it prints 'Draw'. If the absolute difference is even, it sets `l` and `r` based on `b` and checks if `d` falls within the range `[l, r]` with a tolerance of `x`. If so, it prints 'Bob'; otherwise, it prints 'Draw'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of six integers (h, w, x_a, y_a, x_b, y_b). For each test case, it determines whether 'Alice', 'Bob', or 'Draw' should be printed based on the values of x_a, y_a, x_b, and y_b. Specifically, if x_a is greater than x_b, it prints 'Draw'. Otherwise, it calculates a midpoint x and checks if the other coordinates fall within certain ranges with a specified tolerance. Depending on these checks, it prints 'Alice', 'Bob', or 'Draw' for each test case.

