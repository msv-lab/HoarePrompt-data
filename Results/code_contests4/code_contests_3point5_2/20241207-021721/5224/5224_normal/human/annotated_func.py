#State of the program right berfore the function call: $N$ is a non-negative integer. Each dataset consists of real numbers $x_a$, $y_a$, $r_a$, $x_b$, $y_b$, and $r_b$.**
def func():
    n = input()
    for i in xrange(n):
        xa, ya, ra, xb, yb, rb = map(int, raw_input().split())
        
        d = (xa - xb) ** 2 + (ya - yb) ** 2
        
        if d > (ra + rb) ** 2:
            print(0)
        elif ra > rb:
            if (ra - rb) ** 2 > d:
                print(2)
            else:
                print(1)
        elif (rb - ra) ** 2 > d:
            print(-2)
        else:
            print(1)
        
    #State of the program after the  for loop has been executed: $N$ is a non-negative integer, $n$ is greater than 0. After all iterations of the loop have finished, the variables $xa, ya, ra, xb, yb, rb, d$ will have their final values based on the input provided. The program will print different values (0, 1, 2, -2) based on the conditions specified in the loop for each set of input values.
#Overall this is what the function does:The function `func` reads input datasets consisting of real numbers $x_a$, $y_a$, $r_a$, $x_b$, $y_b$, and $r_b. It then calculates the distance between two points (xa, ya) and (xb, yb) and compares it with the sum and difference of their respective radii to determine different outcomes (0, 1, 2, -2) based on specific conditions. The function repeats this process for each dataset provided.

