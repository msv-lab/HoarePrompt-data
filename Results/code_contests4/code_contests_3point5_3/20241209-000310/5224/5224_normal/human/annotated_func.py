#State of the program right berfore the function call: 
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer for the loop to execute; `xa, ya, ra, xb, yb, rb, d` have specific integer values based on the input. The loop will execute for `n` iterations, and at the end of each iteration, the values of `xa, ya, ra, xb, yb, rb, d` will be updated based on the new input values. The final output will be based on the conditions met in each iteration.
#Overall this is what the function does:The function takes input for the number of iterations `n` and then iterates `n` times. For each iteration, it calculates the distance between two points, checks specific conditions based on the radii of two circles, and prints a corresponding integer value. The function does not accept any parameters and does not return anything.

