#State of the program right berfore the function call: The function `func` takes no arguments but operates on input provided through standard input. The input begins with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases. Each of the following t lines contains two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively, for that test case.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: A series of integers, each representing the computed value of `z` for each test case.
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers representing the number of 1x1 and 2x2 application icons. For each test case, it calculates and prints the minimum number of 2x2 grids required to cover all the icons.

