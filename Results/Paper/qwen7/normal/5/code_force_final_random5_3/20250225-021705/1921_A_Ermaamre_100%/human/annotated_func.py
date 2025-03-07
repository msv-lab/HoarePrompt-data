#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. There are t testcases where 1 ≤ t ≤ 100, and it is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: After all iterations of the loop have finished, `t` will be equal to the number of test cases entered by the user. `a` will be a list containing 4 lists for each test case, where each of these 4 lists contains integers entered by the user. For each test case, `x` will be a list containing the first element from each of the 4 lists in `a`. The variable `dx` will be the difference between the maximum and minimum values in the list `x` for each test case. Finally, the loop will print the square of `dx` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four points defining a square with sides parallel to the coordinate axes. It calculates the side length of each square (the difference between the maximum and minimum x-coordinates) and prints the square of this side length for each test case. The function does not return any value but prints the results directly.

