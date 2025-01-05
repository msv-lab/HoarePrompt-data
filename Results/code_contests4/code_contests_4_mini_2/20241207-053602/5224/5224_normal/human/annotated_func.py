#State of the program right berfore the function call: N is a non-negative integer such that 1 <= N <= 50, and each dataset consists of real numbers representing the coordinates (x_a, y_a) and (x_b, y_b) of the centers of circles A and B, as well as their respective radii (r_a, r_b).
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer such that 1 <= N <= 50; `n` is a string that converts to an integer greater than or equal to 1; `i` is `N` - 1 after all iterations; `xa`, `ya`, `ra`, `xb`, `yb`, `rb` are assigned values from the input during the loop execution; `d` is calculated as (xa - xb) for each iteration; the printed outputs correspond to the conditions evaluated based on `d`, `ra`, and `rb` for each pair of inputs processed.
#Overall this is what the function does:The function processes multiple datasets of two circles defined by their centers' coordinates and radii. For each dataset, it determines the relationship between the two circles and prints the following results: 0 if the circles are separate, 2 if circle A is completely inside circle B, -2 if circle B is completely inside circle A, and 1 if the circles overlap or touch. The function accepts a non-negative integer N as input, which specifies the number of datasets to process, and does not return any values; it directly prints the results for each dataset.

