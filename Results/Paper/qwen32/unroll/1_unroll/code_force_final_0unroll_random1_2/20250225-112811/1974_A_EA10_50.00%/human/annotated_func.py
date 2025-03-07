#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The values of `x` and `y` will be those from the last test case, and `z` and `m` will be the values calculated in the last iteration of the loop. The value of `a` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` representing the number of 1x1 and 2x2 application icons, respectively. It then calculates and prints the total number of icons needed for each test case.

