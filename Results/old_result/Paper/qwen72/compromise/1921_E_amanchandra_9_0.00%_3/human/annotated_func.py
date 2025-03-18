#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. The inputs are such that `1 <= h <= 10^6`, `1 <= w <= 10^9`, `1 <= x_a, x_b <= h`, `1 <= y_a, y_b <= w`, and the initial positions of Alice's and Bob's chips do not coincide (`x_a != x_b` or `y_a != y_b`). Additionally, the sum of `h` over all test cases does not exceed `10^6`.
def func():
    for i in range(int(input())):
        h, w, xa, ya, xb, yb = map(int, input().split())
        
        if xa > xb:
            print('Draw')
        else:
            x = abs(xa - xb) // 2
            if abs(xa - xb) % 2:
                l = max(1, yb - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Alice'])[abs(l - ya) <= x + 1 and abs(r - ya) <=
                    x + 1])
            else:
                l = max(1, ya - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Bob'])[abs(l - yb) <= x and abs(r - yb) <= x])
        
    #State: The loop processes all test cases and prints the result for each case as either 'Draw', 'Alice', or 'Bob' based on the conditions specified in the loop. The variables `h`, `w`, `xa`, `ya`, `xb`, and `yb` are reset and re-assigned for each test case, and their final values are the ones from the last test case processed. The loop itself does not modify any other variables outside its scope.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a grid defined by dimensions `h` and `w`, and the initial positions of two chips (Alice's and Bob's) on this grid, given by coordinates `(x_a, y_a)` and `(x_b, y_b)`. For each test case, the function determines and prints the result as either 'Draw', 'Alice', or 'Bob' based on the relative positions of the chips and the grid dimensions. The final state of the function is that all test cases have been processed, and the result for each case has been printed. The variables `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b` are reset and re-assigned for each test case, and their final values are those from the last test case processed.

