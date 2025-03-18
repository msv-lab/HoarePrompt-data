#State of the program right berfore the function call: There are four lines, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: Output State: The value of `t` must be greater than 0, `a` is a 4x4 matrix of integers entered by the user for each iteration, `x` is a list of the first element from each of the 4 lists in `a` for each iteration, and `dx` is the difference between the maximum and minimum values in `x` for each iteration. The final output will be the result of `dx * dx` printed for each of the `t` iterations, concatenated together if `t` is greater than 1.
    #
    #This means that after all iterations of the loop have finished, the output will consist of `t` lines, each line displaying the result of `dx * dx` for that particular iteration.
#Overall this is what the function does:The function reads multiple sets of coordinates from the user, where each set represents the corners of a square. For each set, it calculates the difference between the maximum and minimum x-coordinates, squares this difference, and prints the result. The function does not return any value but prints the calculated results for each set of coordinates.

