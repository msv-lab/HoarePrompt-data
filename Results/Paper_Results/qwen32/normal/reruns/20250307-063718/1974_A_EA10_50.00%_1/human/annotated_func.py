#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: the output state you calculate.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the counts of 1x1 and 2x2 application icons. For each test case, it calculates and prints the minimum number of 2x2 grid units required to cover all the icons.

