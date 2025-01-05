#State of the program right berfore the function call: Each dataset consists of real numbers representing the coordinates and radius of two circles A and B.**
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
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop, `n`, `xa`, `ya`, `ra`, `xb`, `yb`, `rb`, `d` are integers. The loop calculates the distance `d` between two circles A and B based on their coordinates and radii. Depending on the relationship between the distances and radii, specific actions are performed.
#Overall this is what the function does:Functionality: The function `func` reads input data representing the coordinates and radii of two circles A and B. It then calculates the distance between the circles and based on the relationship between the circles, it prints out specific results. If Circle A is completely inside Circle B, it prints 0. If Circle B is completely inside Circle A, it prints -2. If the circles intersect but do not completely contain each other, it prints 1 or 2 depending on the radii. The function handles comparisons between the circles to determine their relationship.

