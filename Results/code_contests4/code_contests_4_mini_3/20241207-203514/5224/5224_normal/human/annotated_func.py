#State of the program right berfore the function call: N is a non-negative integer less than or equal to 50, and each dataset consists of six real numbers (x_a, y_a, r_a, x_b, y_b, r_b) representing the coordinates and radii of circles A and B.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer less than or equal to 50; `i` is equal to `N`; `xa`, `ya`, `ra`, `xb`, `yb`, `rb` are assigned values from input corresponding to each iteration; `d` is calculated as (xa - xb)² + (ya - yb)² for each iteration. The output printed during the loop will be based on the comparisons of `d`, `ra`, and `rb` for each pair of inputs.
#Overall this is what the function does:The function accepts a non-negative integer `n` (less than or equal to 50), which represents the number of datasets. For each dataset, it reads six integers representing the coordinates and radii of two circles (A and B). It calculates the squared distance `d` between the centers of the circles and compares this distance with the sum and difference of their radii to determine their relationship. The output for each dataset is as follows: if the circles are separate, it prints 0; if circle A contains circle B, it prints 2; if circle B contains circle A, it prints -2; if the circles intersect, it prints 1. The function does not return any values but prints results directly to the console for each dataset processed.

