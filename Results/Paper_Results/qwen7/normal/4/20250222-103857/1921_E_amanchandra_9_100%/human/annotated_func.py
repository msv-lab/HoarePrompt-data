#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
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
        
    #State: t is 0, r is the minimum of w and either d + x (if x is odd) or b + x (if x is even), w, a, b, c, d, x, and l are updated to the values from the last input, regardless of whether a > c or not.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six integers \(h\), \(w\), \(x_a\), \(y_a\), \(x_b\), and \(y_b\). For each test case, it compares \(x_a\) and \(x_b\). If \(x_a > x_b\), it prints 'Draw'. Otherwise, it calculates the possible range for \(x\) based on the difference between \(a\) and \(c\). Depending on whether this difference is odd or even, it determines a range for \(x\) and checks if \(b\) or \(d\) falls within this range. Based on these conditions, it prints either 'Draw', 'Alice', or 'Bob'. After processing all test cases, the function prints nothing and ends.

