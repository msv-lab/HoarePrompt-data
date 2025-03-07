#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9, and the positions (x_a, y_a) and (x_b, y_b) are distinct. The sum of h over all test cases does not exceed 10^6.
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
        
    #State: `t` is 0; `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b` remain as initially described.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a rectangle with dimensions `h` and `w`, and two distinct positions `(x_a, y_a)` and `(x_b, y_b)` within the rectangle. For each test case, it determines and prints the result of a game where two players, Alice and Bob, are positioned at `(x_a, y_a)` and `(x_b, y_b)` respectively. The result can be 'Alice', 'Bob', or 'Draw', based on their positions relative to each other and the dimensions of the rectangle.

