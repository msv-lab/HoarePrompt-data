#State of the program right berfore the function call: N is a non-negative integer less than or equal to 50, and each dataset consists of real numbers x_a, y_a, r_a, x_b, y_b, r_b, representing the center coordinates and radii of circles A and B, respectively.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer less than or equal to 50; `i` is `N`; `d` is calculated based on the last values of `xa`, `xb`, `ya`, and `yb` from the last iteration; the outputs printed during the loop execution depend on the comparisons of `d`, `ra`, and `rb` across all iterations.
#Overall this is what the function does:The function accepts a non-negative integer N (where N ≤ 50) and processes N datasets, each consisting of two circles defined by their center coordinates (xa, ya) and (xb, yb) and their radii (ra and rb). It calculates the squared distance between the centers of the circles and determines their spatial relationship, printing the following results for each dataset: "0" if the circles are separate, "2" if circle A is completely within circle B, "-2" if circle B is completely within circle A, and "1" if the circles intersect or touch. The function does not return any value but outputs results directly.

