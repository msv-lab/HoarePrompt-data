#State of the program right berfore the function call: N is a non-negative integer less than or equal to 50, and each dataset consists of real numbers representing the coordinates (x_a, y_a) and (x_b, y_b) as well as the radii (r_a, r_b) of circles A and B.
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
        
    #State of the program after the  for loop has been executed: `N` is a non-negative integer less than or equal to 50; `n` is a positive integer; `i` is equal to `n`.
#Overall this is what the function does:The function accepts multiple sets of inputs where each set contains the coordinates and radii of two circles. It evaluates the geometric relationship between the two circles based on their positions and sizes, outputting 0 if they are separate, 1 if they are tangent, 2 if one circle is within the other, and -2 if the second circle is within the first. The function can handle up to 50 sets of input.

