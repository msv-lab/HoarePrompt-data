#State of the program right berfore the function call: The input consists of an integer N (0 < N <= 50) followed by N lines, each containing six real numbers: x_a, y_a, r_a, x_b, y_b, r_b, where (x_a, y_a) and (x_b, y_b) are the coordinates of the centers of circles A and B respectively, and r_a and r_b are the radii of circles A and B, respectively.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `i` is `n`, `xa`, `ya`, `ra`, `xb`, `yb`, `rb` are input integers for each iteration, and `d` is calculated as (xa - xb)² + (ya - yb)² for each iteration. The output for each iteration depends on the conditions checked in the loop, producing either 0, 1, 2, or -2.
#Overall this is what the function does:The function accepts an integer N (where 0 < N <= 50) and processes N sets of input data, each containing the coordinates and radii of two circles. For each pair of circles, it calculates the distance between their centers and determines their spatial relationship. It outputs 0 if the circles do not overlap, 1 if they touch or intersect, 2 if one circle is completely inside the other without touching, and -2 if the second circle is completely inside the first without touching. The function handles input and output directly without returning any values.

