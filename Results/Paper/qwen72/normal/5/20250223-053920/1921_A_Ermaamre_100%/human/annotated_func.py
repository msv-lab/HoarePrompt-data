#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of 4 tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates x_i, y_i are within the range -1000 to 1000, and the square has a positive area with sides parallel to the coordinate axes. The number of test cases, t, is an integer such that 1 <= t <= 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: For each test case, the loop prints the area of the largest square that can be formed using the given coordinates. The variable `t` remains unchanged, and the list of test cases is also unchanged. The loop iterates `t` times, and for each iteration, it reads the coordinates of a square, calculates the side length of the square by finding the maximum and minimum x-coordinates, and then prints the area of the square (side length squared).
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it reads 4 tuples of coordinates (x_i, y_i) from the input, where each tuple represents a corner of a square. The function then calculates the side length of the square by finding the difference between the maximum and minimum x-coordinates and prints the area of the square (side length squared). The function does not return any value; it only prints the area for each test case. The variable `t` remains unchanged, and the input coordinates are not stored or modified after processing.

